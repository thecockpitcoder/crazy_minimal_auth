from django.shortcuts import render
from django.views import View


# Create your views here.


def HomePage(request):
    return render(request, 'core/index.html')