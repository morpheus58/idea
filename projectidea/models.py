__author__ = 'Morya Jr'

from django.db import models
from django.utils import timezone

class Idea(models.Model):
    categories = (
        ('Tech','Technology'), ('Environment', 'Environment'),
        ('Shopping', 'Shopping'),('People', 'People') ,
        ('Financial','Financial'), ('Writing', 'Writing'))
    title = models.CharField(max_length=100)
    idea = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    updated_last = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=20, choices=categories)
    sentiment = models.CharField(max_length=100, default='')

    def publish(self):
        self.published_at = timezone.now()
        self.updated_last = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    #def update(self, instance):
     #   self.updated_last = timezone.now()
      #  self.idea
