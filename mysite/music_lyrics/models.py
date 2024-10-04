# music_lyrics/models.py

from django.db import models

class Lyrics(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    lyrics = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.artist}"