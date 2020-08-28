from django.shortcuts import render, get_object_or_404
from .models import Job, Project,Stack
# Create your views here.
def home(request):
    jobs = Job.objects
    projects= Project.objects
    skills = Stack.objects
    return render(request,'jobs/home.html',{'jobs':jobs,'projects':projects,'skills':skills})

def detail(request, job_id):
    job_detail = get_object_or_404(Job,pk=job_id)
    return render(request,'jobs/detail.html',{'job':job_detail})