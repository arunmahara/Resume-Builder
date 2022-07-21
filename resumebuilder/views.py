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
            # name = request.POST['name']
            # gender = request.POST['gender']
            # address = request.POST['address']
            # email = request.POST['email']
            # social = request.POST['social']
            # number = request.POST['number']
            # title = request.POST['title']
            # objective = request.POST['objective']
            # company_name = request.POST['company_name']
            # job_title = request.POST['job_title']
            # job_date_form = request.POST['job_date_form']
            # job_date_to = request.POST['job_date_to']
            # college_name = request.POST['college_name']
            # course = request.POST['course']
            # gpa = request.POST['gpa']
            # skills = request.POST['skills']
            # profile_picture = request.POST['profile_picture']
            fm.save()
            messages.success(request, 'Successfully Saved')
    else:
        fm = ProfileForm()
    return render (request, 'index.html', {'form':fm})
