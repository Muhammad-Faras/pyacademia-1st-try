from django.urls import path,include
from .views import HomeTemplateView, NetworkTemplateView 
app_name = 'home'
urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('network/', NetworkTemplateView.as_view(), name='network')
]