from django.urls import path

from . import views

app_name = "propAMC"

urlpatterns = [
    path('', views.index, name='index'),
]