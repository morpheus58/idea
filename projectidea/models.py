__author__ = 'Morya Jr'

from django.db import models
from django.utils import timezone
class Category(models.Model):
    categories = (
        ('Tech','Technology'), ('Environment', 'Environment'),
        ('Shopping', 'Shopping'),('People', 'People') ,
        ('Financial','Financial'), ('Writing', 'Writing'))
    name = models.CharField(max_length=20, choices=categories)


class Idea(models.Model):
    title = models.CharField(max_length=100)
    idea = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    updated_last = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('auth.User')
    category = models.ManyToManyField(Category)
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
