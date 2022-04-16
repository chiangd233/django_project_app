from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Workout, Exercise

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
    template_name = "workout_create.html"

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/')

class Workout_Detail(DetailView):
    model = Workout
    template_name = "workout_detail.html"

class Workout_Update(UpdateView):
    model = Workout
    fields = ['name', 'intensity', 'rounds', 'time', 'exercise']
    template_name = "workout_create.html"
    def get_success_url(self):
        return reverse('park_detail', kwargs = {'pk': self.object.pk})

class Workout_Delete(DeleteView):
    model = Workout
    template_name = "workout_delete_confirm.html"
    success_url = "/"

def profile(request, username):
    user = User.objects.get(username = username)
    workouts = Workout.objects.filter(user = user)
    return render(request, 'profile.html', {'username': username, 'workouts': workouts})

class Exercise(TemplateView):
    exercise = Exercise.objects.all()
    return render(request, 'exercise.html', {'exercise': exercise})

class Exercise_Create(CreateView):
    model = Exercise
    fields = ['number', 'exercise', 'body']
    template_name = "exercise_create.html"

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/')

class Exercise_Delete(DeleteView):
    model = Exercise
    template_name = "exercise_delete_confirm.html"
    success_url = "/"