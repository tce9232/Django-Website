from django.urls import path
from django.conf.urls import include
from django.contrib import admin


from . import views

app_name = 'category'
urlpatterns = [
    path('<slug:category>/', views.category_view, name='category'),
]