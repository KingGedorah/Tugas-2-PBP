from django.db import models

# Create your models here.
class WatchListItem(models.Model):
    status = models.CharField(max_length=20)
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.CharField(max_length=20)
    review = models.TextField()