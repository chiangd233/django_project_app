from django.shortcuts import render
from django.views.generic.base import TemplateView
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