from django.shortcuts import render
from django.http import HttpResponse
from getTwitterData import TwitterFetcher

def home(request):
	return render(request, 'html/home.html', {})

def responce(request):
	hashtags = False
	error = True
	twitter = TwitterFetcher()
	for query in request.GET:
		q = request.GET.getlist(query)
		for user in q:
			if user:
				error = False
				twitter.addUser(user)
	hashtags = twitter.getHashtags(twitter.getUsersTweets())
	mentions = twitter.getMentions(twitter.getUsersTweets())
	return render(request, 'html/home.html', {'error': error, 'hashtags': hashtags, 'mentions': mentions})