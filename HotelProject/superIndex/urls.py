from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from superIndex import views
from django.contrib.auth import views as auth_views

app_name = 'superIndex'
urlpatterns = [
    url(r'^standard_room/$',views.standard_room,name='standard_room'),
    url(r'^registration/$',views.registration,name='registration'),
    url(r'^luxury_room/$',views.luxury_room,name='luxury_room'),
    url(r'^login/$',views.user_login,name='login'),
]
