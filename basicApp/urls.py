from django.urls import path
from . import views

app_name = 'basicApp'

urlpatterns = [
    path('', views.index, name='home'),
    path('/contact', views.contact, name='contact'),
    path('/register', views.register, name='register'),
    path('/logout', views.user_logout, name='user_logout'),
    path("/special", views.special, name='special'),
    path("/user_login", views.user_login, name='user_login'),

]
