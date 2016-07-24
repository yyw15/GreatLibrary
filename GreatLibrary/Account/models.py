from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserInfo(models.Model):
	name 		= models.CharField(max_length=20)
	password 	= models.CharField(max_length=50)
	gender 		= models.CharField(max_length=10, default="male")
	phone 		= models.IntegerField(default=000-0000-0000)
	info 		= models.CharField(max_length=255, default="your information")
	email 		= models.EmailField()
	score 		= models.FloatField(default=0)
	isAdmin 	= models.BooleanField(default=False)
	isBlocked 	= models.BooleanField(default=True)

	def __str__(self):
		return self.name