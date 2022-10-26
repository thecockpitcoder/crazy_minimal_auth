from django.urls import path
from core.views import HomePage

urlpatterns = [
    path('', HomePage, name='homepage'),
]