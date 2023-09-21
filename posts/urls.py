from django.urls import path

from APS_Project2 import settings
from . import views
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    path('', views.posts, name='posts'),
    path('uploadpost/', views.uploadpost, name='uploadpost'),
    path('deletepost/<str:pk>/', views.deletepost, name='deletepost'),
    path('editpost/<str:pk>/', views.editpost, name='editpost'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    