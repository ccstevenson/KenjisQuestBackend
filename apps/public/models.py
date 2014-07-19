from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=50, unique=True)
    logo = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(default="", null=True, blank=True)
    phone = models.TextField(default="", null=True, blank=True)
    website = models.TextField(default="", null=True, blank=True)
    email = models.TextField(default="", null=True, blank=True)

    def __unicode__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=50, unique=True)
    username = models.TextField(default="", null=True, blank=True)
    password = models.TextField(default="", null=True, blank=True)
    emailAddress = models.TextField(default="", null=True, blank=True)
    Business = models.ManyToManyField('Business', null=True, blank=True)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50, unique=True)
    username = models.TextField(default="", null=True, blank=True)
    password = models.TextField(default="", null=True, blank=True)
    emailAddress = models.TextField(default="", null=True, blank=True)
    Business = models.ManyToManyField('Business', null=False, blank=False)

    def __unicode__(self):
        return self.name


class Todo(models.Model):
    name = models.CharField(max_length=50)
    Business = models.ManyToManyField('Business', null=False, blank=False)

    class Meta:
        verbose_name_plural = "Todos"

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField(default=1.00, null=True, blank=True)
    num_in_stock = models.IntegerField(default=0, null=True, blank=True)
    image_path = models.CharField(max_length=50, null=True, blank=True) #referencing an image path until functionality is added to upload a photo
    Business = models.ManyToManyField('Business', null=False, blank=False)

    def __unicode__(self):
        return self.name