from django.db import models


class User(models.Model):
    name = models.CharField(default='', max_length=50)
    username = models.CharField(default='', max_length=50, unique=True)
    password = models.CharField(default='', max_length=50)
    email = models.EmailField(default='',)
    USER_TYPES = (
        ('0', ''),
        ('1', 'Player'),
        ('2', 'DM')
    )
    type = models.CharField(default='', choices=USER_TYPES,  max_length=50, unique=True)
    characters = models.OneToOneField('Character', null=True, blank=True)

    def __unicode__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=50, unique=True)
    owner = models.OneToOneField('User', null=True, blank=True)
    active = models.BooleanField(default=False,)
    hit_points = models.IntegerField(default=0)
    race = models.OneToOneField('Race', null=True, blank=True)
    nationality = models.OneToOneField('Nationality', null=True, blank=True)
    items = models.ManyToManyField('Item', null=True, blank=True)
    weapons = models.ManyToManyField('Weapon', null=True, blank=True)
    skills = models.ManyToManyField('Skill', null=True, blank=True)

    def __unicode__(self):
        return self.name


class Enemy(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=50, unique=True)
    players = models.ManyToManyField('User', null=True, blank=True)
    scenario = models.OneToOneField('Scenario',  null=True, blank=True)

    def __unicode__(self):
        return self.name


class Scenario(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Nationality(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name