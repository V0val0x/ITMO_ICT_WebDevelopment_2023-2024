from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class ProfessionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)

    def create(self, validated_data):
        return Profession.objects.create(**validated_data)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description']


class SkillOfWarriorSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = SkillOfWarrior
        fields = ['skill', 'level']


class WarriorFullInfoSerializer(serializers.ModelSerializer):
    profession = ProfessionCreateSerializer()
    skill_of_warriors = SkillOfWarriorSerializer(many=True, read_only=True, source='skillofwarrior_set')

    class Meta:
        model = Warrior
        fields = ['id', 'race', 'name', 'level', 'profession', 'skill_of_warriors']
