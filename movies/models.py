from django.db import models
import uuid
from django.contrib.auth.models import User

class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)  # Unique identifier from api
    name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255, blank=True)  # Optional
    image_url = models.URLField(blank=True)
    premiered = models.DateField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)  # Optional
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    
class WatchListMovie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.RESTRICT)  # Assuming a 'Show' model exists
    watch_status = models.CharField(max_length=20, choices=(
        ('WATCHED', 'Watched'),
        ('TO_WATCH', 'To Watch'),
    ))
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.movie.name