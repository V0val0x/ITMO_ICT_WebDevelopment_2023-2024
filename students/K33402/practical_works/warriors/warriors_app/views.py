from rest_framework.decorators import action
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .serializers import *


class WarriorViewSet(ViewSet):
    def list(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})

    @action(detail=False, methods=['get'])
    def get_full_info(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorFullInfoSerializer(warriors, many=True)
        return Response({"WarriorsFullInfo": serializer.data})

    @action(detail=True, methods=['get'])
    def get_warrior_info(self, request, pk=None):
        warrior = get_object_or_404(Warrior, id=pk)
        serializer = WarriorFullInfoSerializer(warrior)
        return Response({"WarriorFullInfo": serializer.data})

    @action(detail=True, methods=['delete'])
    def delete_warrior(self, request, pk=None):
        warrior = get_object_or_404(Warrior, id=pk)
        warrior.delete()
        return Response({"Success": "Warrior with id {} deleted successfully.".format(pk)})

    @action(detail=True, methods=['put'])
    def edit_warrior(self, request, pk=None):
        warrior = get_object_or_404(Warrior, id=pk)
        serializer = WarriorFullInfoSerializer(warrior, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"Success": "Warrior with id {} edited successfully.".format(pk)})


class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionCreateSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class SkillCreateView(APIView):
    def post(self, request):
        serializer = SkillSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillListView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
