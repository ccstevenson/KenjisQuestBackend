from rest_framework import serializers
from models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality