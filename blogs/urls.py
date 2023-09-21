from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('writeblogs/', views.writeblogs, name='writeblogs'),
    path('editblogs/<str:pk>/', views.editblogs, name='editblogs'),
    path('deleteblogs/<str:pk>/', views.deleteblogs, name='deleteblogs'),
    path('readblogs/<str:pk>/', views.readblogs, name='readblogs'),
]