from django.db import models
from django.db.models.fields import DateField
from django.contrib.auth.models import User
import uuid


class POST(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=False)
    category = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField()
    date = models.DateTimeField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    def __str__(self) -> str:
        return self.title
