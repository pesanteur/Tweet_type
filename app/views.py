from flask import render_template, redirect, url_for, request
from app import app
from .models import User
from check_tweets import check_tweets
from tweepy import TweepError

# Set "homepage" to index.html
@app.route('/')
def index():
	return render_template('index.html')

# Save username to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
	username = None
	if request.method == 'POST':
		username = request.form['username']
		# Check that username has not already been searched (not a great query, but works)
		try:
			score = check_tweets(username)[0]
		except TweepError:
			score = "Sorry this username does not exist"
		return render_template('success.html',
					        score=score)
	return render_template('index.html')
