from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date_added = models.DateField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    body = RichTextField()

    def __str__(self):
        return self.title
