from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"