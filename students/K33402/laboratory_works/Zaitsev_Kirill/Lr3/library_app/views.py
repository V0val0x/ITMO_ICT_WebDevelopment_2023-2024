import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from library_app.serializers import *
from library_app.models import *
from rest_framework.permissions import SAFE_METHODS
from . import serializers
from .utils import get_tokens_for_user
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class ReadingRoomViewSet(ModelViewSet):
    queryset = ReadingRoom.objects.all()
    serializer_class = ReadingRoomSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["GET"])
    def show_readers(self, request, pk=None):
        obj = self.get_object()
        qs = Reader.objects.filter(reading_room=obj.id)
        ser = serializers.ReaderSerializer(qs, many=True)
        return Response(ser.data)


class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    #permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'])
    def show_taken(self, request, pk=None):
        obj = self.get_object()
        qs = BookTake.objects.filter(reader=obj.id)
        ser = serializers.ShowBookTakeSerializer(qs, many=True)
        return Response(ser.data)

    @action(detail=False, methods=['GET'])
    def youngest(self, request):
        date = datetime.date.today() - datetime.timedelta(days=(365*20))
        ser = self.get_serializer(self.queryset.filter(birth_date__gt=date), many=True)
        return Response(ser.data)

    @action(detail=False, methods=['GET'])
    def percentage(self, request):
        data = {
            'всего': self.queryset.count(),
            "начальное": self.queryset.filter(education='Начальное').count(),
            "среднее": self.queryset.filter(education='Среднее').count(),
            "высшее": self.queryset.filter(education='Высшее').count(),
        }
        return Response(data)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["list"]:
            return ShowBookSerializer
        return BookSerializer

    @action(detail=False, methods=['GET'])
    def take_unique_books(self, request):
        res_qs = BookTake.objects.none()
        for obj in self.queryset:
            count = BookCopy.objects.filter(book=obj.id).count()
            if count <= 2:
                res_qs |= BookTake.objects.filter(book_copy__book=obj.id)
        return Response(ShowBookTakeSerializer(res_qs, many=True).data)


class BookCopyViewSet(ModelViewSet):
    queryset = BookCopy.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["list"]:
            return ShowBookCopySerializer
        return BookCopySerializer


class BookTakeViewSet(ModelViewSet):
    queryset = BookTake.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'take_last_month']:
            return ShowBookTakeSerializer
        return BookTakeSerializer

    @action(detail=False, methods=['GET'])
    def take_last_month(self, request):
        date = datetime.date.today() - datetime.timedelta(weeks=4)
        qs = self.queryset.filter(take_date__lt=date)
        ser = self.get_serializer(qs, many=True)
        return Response(ser.data)


######################


class RegistrationView(generics.CreateAPIView):
    serializer_class = serializers.RegistrationSerializer
    queryset = User.objects.all()


class LoginView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        if 'username' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                auth_data = get_tokens_for_user(request.user)
                return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
            return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    serializer_class = serializers.LogoutSerializer
    queryset = User.objects.all()

    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = serializers.PasswordChangeSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)