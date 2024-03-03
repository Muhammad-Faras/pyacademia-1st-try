from django.urls import path,include
from .views import feedview
app_name = 'feed'
urlpatterns = [
    path('',feedview,name='feed'),
] 