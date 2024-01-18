# ratings/models.py
from django.db import models
from django.utils.timesince import timesince
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Rate(models.Model):
    value = models.IntegerField(default=0,
                                validators=[
                                    MinValueValidator(0, message="Rating must be at least 0."),
                                    MaxValueValidator(5, message="Rating must be at most 5."),
                                ])
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='ratings', null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def created_at_formatted(self):
        return timesince(self.created_at)


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    is_private = models.BooleanField(default=False)

    total_value_raw_rate = models.IntegerField(default=0)
    rate_count = models.IntegerField(default=0)

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    @property
    def average_rate(self):
        return self.total_value_raw_rate / self.rate_count

    class Meta:
        ordering = ('-created_at',)

    def created_at_formatted(self):
        return timesince(self.created_at)
