from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


class Advertisement(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='OPEN')
    author = models.ForeignKey(User, related_name='advertisements', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.status == 'OPEN' and Advertisement.objects.filter(author=self.author, status='OPEN').count() >= 10:
            raise ValidationError('You cannot have more than 10 open advertisements.')
        super().save(*args, **kwargs)