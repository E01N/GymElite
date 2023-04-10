# Generated by Django 3.2 on 2023-03-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_planner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=1),
        ),
    ]