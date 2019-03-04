from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=datetime.now())


	def __str__(self):
		return self.tutorial_title


class Post(models.Model):
		title = models.CharField(max_length=200)
		body = models.TextField()
		username = models.ForeignKey(User,  on_delete="cascade")
		published = models.DateTimeField("date published", default=datetime.now())
