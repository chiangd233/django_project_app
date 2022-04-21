from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
        return reverse('workout_detail', kwargs = {'pk': self.object.pk})

class Workout_Delete(DeleteView):
    model = Workout
    template_name = "workout_delete_confirm.html"
    success_url = "/"

def profile(request, username):
    user = User.objects.get(username = username)
    workouts = Workout.objects.filter(user = user)
    return render(request, 'profile.html', {'username': username, 'workouts': workouts})

def Exercise_Index(request):
    exercise = Exercise.objects.all()
    return render(request, 'exercise.html', {'exercise': exercise})

class Exercise_Create(CreateView):
    model = Exercise
    fields = ['number', 'name', 'body']
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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'signup.html', {'form': form})    
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
                    return render(request, 'login.html', {'form': form})
            else:
                print('The username and/or password is incorrect.')
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else: 
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})