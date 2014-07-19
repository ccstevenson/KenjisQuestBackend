
from rest_framework import generics
from serializers import *
from models import *


class BusinessList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Business
    serializer_class = NestedBusinessSerializer
    queryset = Business.objects.all()


class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Business
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()


class CreateBusiness(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Business
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()


class OwnerList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Owner
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class OwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Owner
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class CreateOwner(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Owner
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class EmployeeList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Employee
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Employee
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class CreateEmployee(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Employee
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class TodoList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Todo
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Todo
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class CreateTodo(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Todo
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class ProductList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CreateProduct(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()