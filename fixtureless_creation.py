import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "kenjis_quest.settings")

from fixtureless import Factory

from apps.public.models import *

objects = [Item, Weapon, Skill, Character, CharacterClass, Player, Race, Nationality, Encounter, Scenario, Chapter, Game]

for object in objects:
    factory = Factory()
    count = 20
    fixture = factory.create(object, count)