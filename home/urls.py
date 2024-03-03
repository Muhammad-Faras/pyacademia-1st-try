from django.urls import path,include
from .views import HomeTemplateView
app_name = 'home'
urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home')
]