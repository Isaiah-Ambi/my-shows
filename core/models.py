from django.db import models
import uuid
from django.contrib.auth.models import User

class Show(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    tvmaze_id = models.IntegerField(unique=True)  # Unique identifier from TVMaze
    name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255, blank=True)  # Optional
    status = models.CharField(max_length=50)  # e.g., "Running", "Ended"
    image_url = models.URLField(blank=True)
    premiered = models.DateField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)  # Optional
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    
class WatchListShow(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey('Show', on_delete=models.RESTRICT)  # Assuming a 'Show' model exists
    watch_status = models.CharField(max_length=20, choices=(
        ('WATCHED', 'Watched'),
        ('CURRENTLY_WATCHING', 'Currently Watching'),
        ('TO_WATCH', 'To Watch'),
    ))
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.show.name