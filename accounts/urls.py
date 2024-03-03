from .views import SignupView
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('signup/',SignupView.as_view(),name = 'signup'),
]
