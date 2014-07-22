from rest_framework import serializers
from models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character


class CharacterClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterClass


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


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        depth = 2

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario


class EncounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encounter


