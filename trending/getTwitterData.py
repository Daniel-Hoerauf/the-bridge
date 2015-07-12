import twitter
from collections import Counter



class TwitterFetcher:
	def __init__(self):
		self.api = twitter.Api(consumer_key='Qry3gBL3fkztLoRzsMTVOkkZQ', consumer_secret='ncBUSXHlCSo83px3rKfc3QNnccZiuWeoe7XFOKVvXtAeNqpFoL', access_token_key='3371085011-TgQOFCSP0twhJ4fgnS9991yQvmX4EYH6lyC11J2', access_token_secret='1V8wT4MIfHK8wjVlUSVcPVNyTmeA1zBBOBG0BgU6Vxopt')
		self.selectedUsers = []

	def getUsersTweets(self):
		statuses = []
		for user in self.selectedUsers:
			status = self.api.GetUserTimeline(screen_name=user, count=50)
			statuses.append(status)
		return statuses

	def getHashtags(self, statuses):
		hashtags = []
		for i in range(0, len(statuses)):
			for status in statuses[i]:
				print status.AsDict()
				if status.AsDict().get('hashtags'):
					for hashtag in status.AsDict().get('hashtags'):
						hashtags.append(hashtag)
		hashtags = Counter(hashtags)
		return hashtags

	def getMentions(self, statuses):
		mentions = []
		for i in range(0, len(statuses)):
			for status in statuses[i]:
				print status.AsDict()
				if status.AsDict().get('user_mentions'):
					for mention in status.AsDict().get('user_mentions'):
						mentions.append(mention.get('screen_name'))
		mentions = Counter(mentions)
		return mentions


	def addUser(self, user):
		self.selectedUsers.append(user)