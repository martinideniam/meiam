from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class projectsPost(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    comment = models.TextField()
    picture = models.ImageField(
        upload_to="gallery", null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
