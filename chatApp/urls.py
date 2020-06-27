from django.urls import path

from chatApp import views
from chatApp.views import index


app_name = 'chat'

urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', views.room, name='room')
]
