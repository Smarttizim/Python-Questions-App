from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import *

class ThemeView(ListView):
    model = Theme
    context_object_name = 'Theme'
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_count'] = self.model.objects.count()
        return context

# def themes_quest(request,id):
#     theme= Theme.objects.get(id=id)
#     theme = theme.themes.all()
#     return render (request ,'about.html',{"theme":theme})


def themes_quest(request,id):
    theme= Theme.objects.get(id=id)
    theme = theme.themes.all()
    print(theme)
    n = 0 
    for i in theme:
        print(i)
        n+= 1
    return render (request ,"about.html",{"theme":theme,"n":n})

class QuestView(ListView):
    model = Quest
    context_object_name = 'quests'
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_count'] = Quest.objects.count() 
        return context


