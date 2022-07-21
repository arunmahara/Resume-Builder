from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProfileForm
from .models import Profile

# Create your views here.
def index(request):
    fm = ProfileForm()
    return render (request, 'index.html', {'form':fm})
