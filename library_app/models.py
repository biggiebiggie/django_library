from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    loan_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title, self.status}"


class Magazine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    loan_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title, self.status}"
