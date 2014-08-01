from django.contrib.auth.models import User
from rest_framework import generics
from serializers import *
from models import *


class UserList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CreateUser(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CharacterList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Character
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Character
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


class CreateCharacter(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Character
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


class CharacterClassList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = CharacterClass
    serializer_class = CharacterClassSerializer
    queryset = CharacterClass.objects.all()


class CharacterClassDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = CharacterClass
    serializer_class = CharacterClassSerializer
    queryset = CharacterClass.objects.all()


class CreateCharacterClass(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = CharacterClass
    serializer_class = CharacterClassSerializer
    queryset = CharacterClass.objects.all()


class WeaponList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Weapon
    serializer_class = WeaponSerializer
    queryset = Weapon.objects.all()


class WeaponDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Weapon
    serializer_class = WeaponSerializer
    queryset = Weapon.objects.all()


class CreateWeapon(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Weapon
    serializer_class = WeaponSerializer
    queryset = Weapon.objects.all()


class ItemList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class CreateItem(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class SkillList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Skill
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Skill
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class CreateSkill(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Skill
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class RaceList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Race
    serializer_class = RaceSerializer
    queryset = Race.objects.all()


class RaceDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Race
    serializer_class = RaceSerializer
    queryset = Race.objects.all()


class CreateRace(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Race
    serializer_class = RaceSerializer
    queryset = Race.objects.all()


class NationalityList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Nationality
    serializer_class = NationalitySerializer
    queryset = Nationality.objects.all()


class NationalityDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Nationality
    serializer_class = NationalitySerializer
    queryset = Nationality.objects.all()


class CreateNationality(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Nationality
    serializer_class = NationalitySerializer
    queryset = Nationality.objects.all()

class GameList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Game
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Game
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class CreateGame(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Game
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class ChapterList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Chapter(generics.CreateAPIView)
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Chapter
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class CreateChapter(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Chapter
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class ScenarioList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Scenario
    serializer_class = ScenarioSerializer
    queryset = Scenario.objects.all()


class ScenarioDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Scenario
    serializer_class = ScenarioSerializer
    queryset = Scenario.objects.all()


class CreateScenario(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Scenario
    serializer_class = ScenarioSerializer
    queryset = Scenario.objects.all()


class EncounterList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Encounter
    serializer_class = EncounterSerializer
    queryset = Encounter.objects.all()


class EncounterDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Encounter
    serializer_class = EncounterSerializer
    queryset = Encounter.objects.all()


class CreateEncounter(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Encounter
    serializer_class = EncounterSerializer
    queryset = Encounter.objects.all()