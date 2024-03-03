from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser_Model(AbstractUser):
    UNIVERSITY_CHOICES = [
        ('gcuf', 'Government College University Faisalabad'),
        ('oxford', 'Oxford University'),
    ]
    
    SKILLS_CHOICES = [
        ('Frontend', 'Frontend Development'),
        ('Backend', 'Backend Development'),
        ('Fullstack', 'FullStack Development'),
        # Add more choices as needed
    ]
    
    university = models.CharField(max_length=100, choices=UNIVERSITY_CHOICES, blank=True)
    skills = models.CharField(max_length=100, choices=SKILLS_CHOICES, blank=True)
