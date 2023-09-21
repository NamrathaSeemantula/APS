from django.urls import path

from APS_Project2 import settings
from . import views
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('special/', views.special, name='special'),
    path('profile/', views.profile, name='profile'),
    path('userslist/', views.userslist, name='userslist'),
    path('viewprofile/<str:pk>/', views.viewprofile, name='viewprofile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    