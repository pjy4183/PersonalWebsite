from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="placeholder.png")
    body = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True,)
    #slug =
    
    def __str__(self):
        return self.headline