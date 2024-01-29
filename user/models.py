from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class UserProfile(models.Model):
    userid = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
