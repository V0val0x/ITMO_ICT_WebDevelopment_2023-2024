from rest_framework import serializers
from django.contrib.auth.models import User
from library_app.models import (Category,
                                Author,
                                ReadingRoom,
                                BookTake,
                                Reader,
                                Book,
                                BookCopy)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class ReadingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingRoom
        fields = "__all__"


class ReaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reader
        fields = "__all__"


####################################


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class ShowBookSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    authors = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'publisher', 'category', 'authors']


class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = "__all__"


class ShowBookCopySerializer(serializers.ModelSerializer):
    book = ShowBookSerializer(read_only=True)

    class Meta:
        model = BookCopy
        fields = ['id',  'book', 'cipher', 'publishing_year']


class BookTakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTake
        fields = '__all__'


class ShowBookTakeSerializer(serializers.ModelSerializer):
    book_copy = ShowBookCopySerializer(read_only=True)
    reader = ReaderSerializer(read_only=True)

    class Meta:
        model = BookTake
        fields = ['id', 'book_copy', 'reader', 'take_date', 'return_date']


####################


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password Does not match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password',]


class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []


class PasswordChangeSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    class Meta:
        model = User
        fields = ['current_password', 'new_password']

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value
