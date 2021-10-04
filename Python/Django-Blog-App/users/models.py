from django.db import models
from django.contrib.auth.models import User
import uuid



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    tagline = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    profession = models.CharField(max_length=200, null=True, blank=True)
    profile_img = models.ImageField(null=True, blank=True)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    social_insta = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    def __str__(self) -> str:
        return self.name

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created=  models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)