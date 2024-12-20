from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    ]
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Upcoming')
    users = models.ManyToManyField(User, related_name='events_registered', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_time'] 
