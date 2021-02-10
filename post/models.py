from django.db import models
from django.conf import settings
# Create your models here.
class Record(models.Model):
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    song_intro = models.TextField()
    song_file = models.FileField(upload_to='musics/', blank=True, null=True, default='')
    song_image = models.FileField(upload_to='images/', blank=True, default='images/default.png')
    published_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    def __str__(self):
        return self.song_title

    #def __str__(self):
    #    return self.song_title + '-' + self.artist

class Comment(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True)
