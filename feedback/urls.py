from django.urls import path, include
from . import views

urlpatterns = [
    path('done', views.done, name='done'),
    path('', views.index, name='index'),
]
