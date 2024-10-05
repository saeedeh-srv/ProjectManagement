from django.shortcuts import render
from .models import Project
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjectListView(LoginRequiredMixin,ListView):
    def get(self,request,*args,**kwargs):
        projects=Project.objects.filter(user=request.user)
        return render(self.request,'projects/projects.html', {'projects': projects})

# Create your views here.
