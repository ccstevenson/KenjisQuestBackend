from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')

    def __unicode__(self):
        return self.name


class Weapon(Item):
    damage = models.CharField(max_length=50, default='')

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')

    def __unicode__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')

    def __unicode__(self):
        return self.name


class Nationality(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Nationalities'


class CharacterClass(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Character Classes'


class Character(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')
    health = models.IntegerField(default=30,)
    maxHealth = models.IntegerField(default=30)
    sprite = models.CharField(max_length=50, default='')
    race = models.ForeignKey(Race, default='')
    nationality = models.ForeignKey(Nationality, default='')
    character_class = models.ForeignKey(CharacterClass, 'name', default='')
    skills = models.ManyToManyField(Skill,)
    inventory = models.ManyToManyField(Item, related_name='characters', default='')
    weapon = models.ForeignKey(Item, 'name', default='')

    def __unicode__(self):
        return self.name


class Player(User):
    character = models.OneToOneField(Character,)

    def __unicode__(self):
        return self.first_name


class Encounter(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')
    items = models.ManyToManyField(Item, default='')
    characters = models.ManyToManyField(Character, default='')

    def __unicode__(self):
        return self.name


class Scenario(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')
    encounters = models.ManyToManyField(Encounter, default='')

    def __unicode__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')
    scenario = models.ManyToManyField(Scenario, default='')

    def __unicode__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')
    players = models.ManyToManyField(Player, default='', related_name='Games')
    game_master = models.ForeignKey(Player, 'username', default='')
    chapters = models.ManyToManyField(Chapter, default='')

    def __unicode__(self):
        return self.name