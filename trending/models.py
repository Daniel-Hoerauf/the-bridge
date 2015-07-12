from django.db import models
import getTwitterData

class User(models.Model):
	tweetID = models.CharField(max_length=200)
	author = models.TextField()
	def __unicode__(self):
		return self.user_text

class SearchResults(models.Model):
	hashtag_text = models.CharField(max_length=200)
	def __unicode__(self):
		return self.user_text


