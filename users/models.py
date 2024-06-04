from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    picture = models.URLField(max_length=200, blank=True, null=True)
    google_id = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.email
