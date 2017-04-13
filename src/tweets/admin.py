from django.contrib import admin

from .forms import TweetModelForm
from .models import Tweet

#admin.site.register(Tweet)

class TweetModelAdmin(admin.ModelAdmin):
    # Allows control over what fields to show, form level validation, etc...
    form = TweetModelForm

    class  Meta:
        model = Tweet

admin.site.register(Tweet, TweetModelAdmin)
