from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.queries, name='queries'),
    path('postquery/', views.postquery, name='postquery'),
    # path('editblogs/<str:pk>/', views.editblogs, name='editblogs'),
    path('deletequery/<str:pk>/', views.deletequery, name='deletequery'),
    path('readanswers/<str:pk>/', views.readanswers, name='readanswers'),
]