import yaml
from datetime import datetime, timedelta
from numpy import random
import matplotlib.pyplot as plt
import json


# This function count the recurrence of term in a list a print ordered dict.
def list_repartition(a_list):
    repartition = dict()
    for i in a_list:
        string = str(i)
        if repartition.get(string) is None:
            repartition.update({string: 1})
        else:
            repartition.update({string: repartition[string] + 1})
    for key in sorted(repartition.keys()):
        print("%s: %s" % (key, repartition[key]))


# Create the probability from a sample of twitter data
total_tweets_sample = 47508
# From midnight to 23H59
numbers_tweet_sample__by_hour = [2208, 2009, 1917, 1878, 1842, 1531, 1549, 1463,
                                 1192, 1102, 1188, 1132, 1203, 1415, 1497, 1946,
                                 2067, 2215, 2665, 4438, 3358, 2759, 2486, 2448]
percent_tweet_hours = [i/total_tweets_sample for i in numbers_tweet_sample__by_hour]

# Open yaml file
try:
    yaml_config = yaml.load(open('config.yaml'))
except NameError:
    print('Yaml file not found. Make sure there is a config.yaml in the directory.')
    exit()

total_days = yaml_config.get('days')

# Create the end date (useless to be deleted later)
try:
    date_begin = yaml_config.get('date')
    date_end = date_begin + timedelta(days=total_days)
except TypeError:
    print("The date as to be like 2018-10-08.")
    exit()

# Create a random date for the tweet
date_list = list()
for i in range(yaml_config.get('tweet_number')):
    random_days = int(random.randint(total_days + 1, size=1)[0])
    random_numbers = int(random.choice(len(percent_tweet_hours), 1, p=percent_tweet_hours)[0])
    random_minute, random_second = int(random.randint(60, size=1)[0]), int(random.randint(60, size=1)[0])

    date = date_begin + timedelta(days=random_days)
    date = datetime(date.year, date.month, date.day) + timedelta(hours=random_numbers, minutes=random_minute,
                                                                 seconds=random_second)
    date_list.append(date)

# Put json burk in a file
with open("result.json", "w") as outfile:
    count = 0
    for i in date_list:
        outfile.write(json.dumps({"index": {"_index": "test", "_type": "_doc", "_id": count}}))
        outfile.write("\n")
        outfile.write(json.dumps({"date": i.isoformat()}))
        outfile.write("\n")
        count += 1
