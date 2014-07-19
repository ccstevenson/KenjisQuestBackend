from django.conf.urls import patterns, url, include
from bizmanage.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('bizmanage.views',
    url(r'^businesses$', BusinessList.as_view(), name='business-list'),
    url(r'^businesses/(?P<pk>[0-9]+)$', BusinessDetail.as_view(), name='business-detail'),
    url(r'^create-business$', CreateBusiness.as_view(), name='create-business'),

    url(r'^owners$', OwnerList.as_view(), name='owner-list'),
    url(r'^owners/(?P<pk>[0-9]+)$', OwnerDetail.as_view(), name='owner-detail'),
    url(r'^create-owners$', CreateOwner.as_view(), name='owner-recipe'),

    url(r'^employees$', EmployeeList.as_view(), name='employee-list'),
    url(r'^employees/(?P<pk>[0-9]+)$', EmployeeDetail.as_view(), name='employee-detail'),
    url(r'^create-employees$', CreateEmployee.as_view(), name='employee-recipe'),

    url(r'^todos$', TodoList.as_view(), name='todo-list'),
    url(r'^todos/(?P<pk>[0-9]+)$', TodoDetail.as_view(), name='todo-detail'),
    url(r'^todos-owners$', CreateTodo.as_view(), name='todo-recipe'),

    url(r'^products$', ProductList.as_view(), name='product-list'),
    url(r'^products/(?P<pk>[0-9]+)$', ProductDetail.as_view(), name='product-detail'),
    url(r'^products-owners$', CreateProduct.as_view(), name='product-recipe'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)