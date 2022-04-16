from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Workout

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["workouts"] = Workout.objects.filter(name__icontains = name)
            context["header"] = f"Searching for {name.capitalize()}"
        else :
            context["workouts"] = Workout.objects.all()
            context["header"] = "All Workouts"
        return context

class About(TemplateView):
    template_name = "about.html"

class Workout_Create(CreateView):
    model = Workout
    fields = ['name', 'intensity', 'rounds', 'time', 'exercise']
    template = "workout_create.html"

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/')