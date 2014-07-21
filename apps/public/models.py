from django.db import models
from django.contrib.auth.models import User


class Enemy(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')

    def __unicode__(self):
        return self.name


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


class Character(models.Model):
    owner = models.ForeignKey(User, 'username', default='')
    name = models.CharField(max_length=50, unique=True, default='')
    is_active = models.BooleanField(default=False)
    race = models.ForeignKey(Race, default='')
    nationality = models.ForeignKey(Nationality, default='')
    hit_points = models.IntegerField(default=0,)
    skills = models.ManyToManyField(Skill,)
    inventory = models.ManyToManyField(Item, default='')

    def __unicode__(self):
        return self.name


class Battle(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')
    enemies = models.ManyToManyField(Enemy,)
    characters = models.ManyToManyField(Character,)

    def __unicode__(self):
        return self.name


class Scenario(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')
    battles = models.ManyToManyField(Battle,)

    def __unicode__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')
    players = models.ManyToManyField(User,)
    scenario = models.ForeignKey(Scenario, default='')
    characters = models.ManyToManyField(Character,)  # from user's active characters

    def __unicode__(self):
        return self.name