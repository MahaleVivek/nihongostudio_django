from django.shortcuts import render
from .models import main

# Create your views here.
def index(request):
    return render(request, "main/index.html", {
        "main" : main.objects.all()
    })