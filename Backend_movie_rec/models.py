from django.db import models
from django.contrib.auth.models import User
class movie_data(models.Model):
  title =  models.CharField(max_length=30)
  movie_id = models.IntegerField()

