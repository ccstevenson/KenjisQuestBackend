from rest_framework import serializers
from models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character


class EnemySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Enemy


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game


class ScenarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scenario


class WeaponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weapon


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill


class RaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Race


class NationalitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nationality