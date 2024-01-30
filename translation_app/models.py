from django.db import models
from django.contrib.auth.models import User


class Bookmark(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    source_string = models.CharField(max_length=3000, db_comment="source string")
    target_string = models.CharField(max_length=3000, db_comment="target string")
    created_at = models.DateTimeField(auto_now_add=True, db_comment="created at")
    deleted = models.BooleanField(default=False, db_comment="deleted")
    deleted_at = models.DateTimeField(null=True, db_comment="deleted at")


class History(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    source_string = models.CharField(max_length=3000, db_comment="source string")
    target_string = models.CharField(max_length=3000, db_comment="target string")
    created_at = models.DateTimeField(auto_now_add=True, db_comment="created at")
    deleted = models.BooleanField(default=False, db_comment="deleted")
    deleted_at = models.DateTimeField(null=True, db_comment="deleted at")


class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    source_string = models.CharField(max_length=3000, db_comment="source string")
    target_string = models.CharField(max_length=3000, db_comment="target string")
    rating = models.IntegerField(db_comment="rating")
    created_at = models.DateTimeField(auto_now_add=True, db_comment="created at")
    deleted = models.BooleanField(default=False, db_comment="deleted")
    deleted_at = models.DateTimeField(null=True, db_comment="deleted at")
