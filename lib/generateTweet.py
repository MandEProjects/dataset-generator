from numpy import random
from datetime import datetime, timedelta
from lib import utilities, tweet


class GenerateTweet:
    def __init__(self, yaml_config):
        try:
            self.date_begin = yaml_config.get('date')
        except TypeError:
            print("The date as to be like 2018-10-08.")
            exit()
        try:
            self.total_days = yaml_config.get('days')
            self.number_tweet = yaml_config.get('tweet_number')
            self.number_user = yaml_config.get('number_user')
            self.users = yaml_config.get('names')
        except:
            print("Verify your yaml file")
            exit()
        self.prob_tweet_hours = utilities.prob_tweets_by_hour()

    def tweet_add_date(self):

        random_days = int(random.randint(self.total_days + 1, size=1)[0])
        random_numbers = int(random.choice(len(self.prob_tweet_hours), 1, p=self.prob_tweet_hours)[0])
        random_minute, random_second = int(random.randint(60, size=1)[0]), int(random.randint(60, size=1)[0])

        date = self.date_begin + timedelta(days=random_days)
        date = datetime(date.year, date.month, date.day) + timedelta(hours=random_numbers, minutes=random_minute,
                                                                     seconds=random_second)
        return date

    def generate_tweet(self):
        tweet_list = list()

        print(len(self.users))
        print(self.users)
        utilities.creation_users(self.number_tweet, self.users)

        for i in range(self.number_tweet):
            tw = tweet.Tweet()
            tw.date = self.tweet_add_date()
            tweet_list.append(tw)

        return tweet_list

