from django.urls import path
from .views import Home

app_name = 'netlixapp'

urlpatterns = [
    path('', Home, name="home"),
]