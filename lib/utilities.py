import json
import random
from lib import people


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
def prob_tweets_by_hour():
    total_tweets_sample = 47508
    # From midnight to 23H59
    numbers_tweet_sample__by_hour = [2208, 2009, 1917, 1878, 1842, 1531, 1549, 1463,
                                     1192, 1102, 1188, 1132, 1203, 1415, 1497, 1946,
                                     2067, 2215, 2665, 4438, 3358, 2759, 2486, 2448]
    return [i / total_tweets_sample for i in numbers_tweet_sample__by_hour]


# Generate burk to insert in elasticsearch
def generate_burk(json_list):
    # Put json burk in a file
    with open("result.json", "w") as outfile:
        count = 0
        for i in json_list:
            outfile.write(json.dumps({"index": {"_index": "test", "_type": "_doc", "_id": count}}))
            outfile.write("\n")
            outfile.write(json.dumps({"date": i.isoformat()}))
            outfile.write("\n")
            count += 1


# Create the users
def creation_users(nbr_users, list_users=[]):
    with open("firstName.txt") as f:
        first_names = f.readlines()
    with open("lastName.txt") as f:
        last_names = f.readlines()

    peoples = list()
    check = set()

    for i in list_users:
        pple = people.People()
        pple.firstName, pple.lastName = i
        peoples.append(pple)
        check.add((pple.firstName, pple.lastName))

    for i in range(nbr_users - len(list_users)):
        pple = people.People()
        pple.firstName = first_names[random.randint(0, len(first_names) - 1)]
        pple.lastName = last_names[random.randint(0, len(last_names) - 1)]
        while (pple.firstName, pple.lastName) in check:
            pple.lastName = last_names[random.randint(0, len(last_names) - 1)]
        check.add((pple.firstName, pple.lastName))
        peoples.append(pple)

    print(len(peoples))
    return peoples


