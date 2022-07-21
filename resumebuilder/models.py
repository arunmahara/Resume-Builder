import django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    social = models.URLField(blank=True)
    number = models.PositiveBigIntegerField()
    objective = models.TextField()
    company_name= models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    job_date_form = models.DateField(auto_now=False, auto_now_add=False)
    job_date_to = models.DateField(auto_now=False, auto_now_add=False)
    college_name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=2, decimal_places=1)
    skills = models.CharField(max_length=150)
    profile_picture = models.ImageField(upload_to = 'pics')




