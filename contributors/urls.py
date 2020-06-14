from django.urls import path
from django.conf.urls import include
from django.contrib import admin

from . import views

app_name = 'contributors'
urlpatterns = [
    path('', views.ContributorView.as_view(), name='contributors'),
    path("<int:pk>/", views.contributor_detail, name="contributor_detail"),
]