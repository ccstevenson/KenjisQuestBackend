from django.db import models
from django.contrib.auth.models import User


class Player(User):

    def __unicode__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=10, unique=True, default='')

    def __unicode__(self):
        return self.name


class Weapon(Item):
    damage = models.CharField(max_length=10, default='')

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=10, unique=True, default='')

    def __unicode__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=10, unique=True, default='')

    def __unicode__(self):
        return self.name


class Nationality(models.Model):
    name = models.CharField(max_length=10, unique=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Nationalities'


class CharacterClass(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')


class Character(models.Model):
    owner = models.ForeignKey(User, 'username', default='')
    name = models.CharField(max_length=10, unique=True, default='')
    is_active = models.BooleanField(default=False)
    race = models.ForeignKey(Race, default='')
    nationality = models.ForeignKey(Nationality, default='')
    character_class = models.ForeignKey(CharacterClass, default='')
    hit_points = models.IntegerField(default=30,)
    skills = models.ManyToManyField(Skill,)
    inventory = models.ManyToManyField(Item, default='')

    def __unicode__(self):
        return self.name


class Encounter(models.Model):
    name = models.CharField(max_length=10, unique=True, default='')
    items = models.ManyToManyField(Item, default='')
    characters = models.ManyToManyField(Character, default='')

    def __unicode__(self):
        return self.name


class Scenario(models.Model):
    name = models.CharField(max_length=10, unique=True, default='')
    encounters = models.ManyToManyField(Encounter, default='')

    def __unicode__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=10, unique=True, default='')
    scenario = models.ManyToManyField(Scenario, default='')

    def __unicode__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=10, unique=True, default='')
    players = models.ManyToManyField(User, default='')
    chapters = models.ManyToManyField(Chapter, default='')

    def __unicode__(self):
        return self.name