from django.urls import path
from django.conf.urls import include
from django.contrib import admin


from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article', views.ArticleView.as_view(), name='article'),
    path('archive', views.ArchiveView.as_view(), name='archive'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('mission', views.MissionView.as_view(), name='mission'),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path('admin/', admin.site.urls)
]