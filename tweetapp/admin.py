from django.contrib import admin
from tweetapp.models import Tweet
# Register your models here.

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display=['user','text','photo','created_at','updated_at']