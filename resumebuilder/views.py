from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import ProfileForm
from .models import Profile

# Create your views here.
def index(request):
    if request.method == 'POST':
        fm = ProfileForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/')
    else:
        fm = ProfileForm()
    resumes = Profile.objects.all()
    return render (request, 'index.html', {'form':fm, 'resume':resumes})

def resume(request, id):
    resumes = Profile.objects.all()
    return render(request, 'resume.html', {'resume':resumes})