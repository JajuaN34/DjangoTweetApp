from django.contrib import admin
from tweetapp.models import Tweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Nickname',{"fields":["nickname"]}),
        ('Message',{"fields":["message"]})
    ]
 #   fields =['nickname','message']

admin.site.register(Tweet,TweetAdmin)