# Generated by Django 4.0.3 on 2022-04-20 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_exercise_workout_exercise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='exercise',
            new_name='name',
        ),
    ]
