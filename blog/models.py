from django.db import models

# Create your models here.

class Post(models.Model):
    #Image
    #author
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    #category
    counted_views = models.IntegerField(default=0) #(default=0)
    status = models.BooleanField(default=False)
    puplished_date = models.BooleanField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
