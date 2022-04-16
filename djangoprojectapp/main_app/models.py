from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

INTENSITY_CHOICES = (
    ('l','low'),
    ('m','moderate'),
    ('h','high')
)

BODY_CHOICES = (
    ('Chest'),
    ('Arms'),
    ('Shoulders'),
    ('Back'),
    ('Abs'),
    ('Legs')
)

# class Exercise(models.Model):
#     number = models.IntegerField()
#     exercise = models.CharField(max_length = 50)
#     body = models.CharField(max_length = 10, choices = BODY_CHOICES)

#     def __str__(self):
#         return self.name



class Workout(models.Model):
    name = models.CharField(max_length = 50)
    intensity = models.CharField(max_length = 10, choices = INTENSITY_CHOICES)
    rounds = models.IntegerField(validators = [MinValueValidator(1)])
    time = models.IntegerField(validators = [MinValueValidator(1)])
    # exercise = models.ManyToManyField(Exercise)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']





