from django.shortcuts import render
from .models import Skill
from django.http import HttpResponse
# from django.views import generic
# Create your views here.


def index(request):
    skill_list = Skill.objects.all()
    context = {'skill_list': skill_list}
    return render(request, 'portfolio/index.html', context)