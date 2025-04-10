from django.contrib import admin
from django.urls import path
from .views import PatoListCreateAPIView

urlpatterns = [
    path('pato/',PatoListCreateAPIView.as_view(), name='pato-list-create')
]
