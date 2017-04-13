from django.conf import settings
from django.db import models

from .validators import no_abc

class Tweet(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140, validators=[no_abc])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #slug_field = models.SlugField(max_length=40)

    def __str__(self):
        return str(self.content)

    """def clean(self, *args, **kwargs):
        content = self.content
        
        if content == "abc":
            raise ValidationError("Cannot be abc")

        return super(Tweet, self).clean(*args, **kwargs)"""
