from django.urls import path
from . import views

urlpatterns = [

    path('',views.welcome, name='welcom'),
    path('user', views.user , name='user')
]