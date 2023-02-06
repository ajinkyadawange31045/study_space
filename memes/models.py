from django.db import models

class Meme(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to='memes/')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comments = models.TextField(default='No comments yet.')
    shares = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
