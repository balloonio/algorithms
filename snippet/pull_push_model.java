// Pull model
news_feed = []
for follow in user.follows:
    tweets = TweetService.get_recent_tweets_from(follow)
    news_feed.merge(tweets)

return news_feed.most_recent_100_tweets

// Push model
tweet = TweetService.create_tweet_from_params(params)
for follower in current_users.followers:
    TweetService.create_news_feed(
        owner_id=follower.id,
        tweet_id=tweet.id,
        created_at=tweet.created_at,
    )

return create_success