from django.urls import path, include
from .views import Messages, CRUD




urlpatterns = [
    path('hello', Messages.getHello, name='getHello'),
    path('users', CRUD.getUsers, name='getUsers')
]