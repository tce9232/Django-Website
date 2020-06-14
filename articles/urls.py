from django.urls import path
from django.conf.urls import include
from django.contrib import admin


from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.ArchiveView.as_view(), name='archive'),
    path("<int:pk>/", views.article_detail, name="article"),
]