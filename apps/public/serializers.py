from rest_framework import serializers
from models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name',)


class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = ('id', 'name',)


class NestedBusinessSerializer(serializers.ModelSerializer):
    owners = BusinessSerializer()
    employees = EmployeeSerializer()

    class Meta:
        model = Business
        fields = ('id', 'name',)


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'name',)


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'name',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name',)
