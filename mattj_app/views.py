from django.shortcuts import render
from django.http import HttpResponse
from mattj_app.models import Experience

def home(request):
    prof_exp = Experience.objects.filter(exp_type = 'professional').order_by("-start_date")
    ed_exp = Experience.objects.filter(exp_type = 'education').order_by("-start_date")
    return render(request, 'home.html',{'professional_experience':prof_exp,'education_experience':ed_exp})
