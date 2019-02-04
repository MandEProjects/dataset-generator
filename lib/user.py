import random
import json
import secrets
import numpy as np
from lib import static
import random as rd


class User:

    def __init__(self, distributions_manager, datasets_manager):
        self.lastName = str()
        self.firstName = str()
        self.age = int(round(distributions_manager.age_distribution.rvs(1)[0]))
        self.followers = int()
        self.probability = int()
        self.favorite_subjects, self.number_of_favorite_subjects = self.define_favorite_subjects(
            distributions_manager.favorite_subjects_per_user_distribution, datasets_manager.list_of_subjects)
        self.occupation, self.compensation = self.define_occupations_and_compensation(distributions_manager.salary_distribution_per_occupation)
        self.followers = int(round(distributions_manager.followers_distribution.rvs(1)[0]))
        self.id = secrets.token_urlsafe()
        self.country = None
        self.country_code2 = None
        self.continent = None
        self.region = None
        self.location = dict()
        self.city = str()

    def elastic_mapping_user_centric(self, list_message):
        sum_likes = sum([message.likes for message in list_message])
        dic = {
            "salary": self.compensation,
            "average_likes": (sum_likes/len(list_message)) if len(list_message) != 0 else 0,
            "number_of_messages": len(list_message),
            "sum_of_likes": sum_likes,
            "list_subjects": [message.subjects for message in list_message],
            "average_time_between": self.message_date_average(list_message)
        }
        dic.update(self.elastic_mapping_message())
        return dic

    def elastic_mapping_message(self):
        dic = {
            "user_id": self.id,
            "last_name": self.lastName,
            "occupation": self.occupation,
            "first_name": self.firstName,
            "age": self.age,
            "followers": self.followers,
            "favorite_subjects": self.favorite_subjects,
            "favorite_subjects_as_string": ' '.join(self.favorite_subjects),
            "number_of_favorite_subjects": self.number_of_favorite_subjects,
            "geo": {
                "country": self.country,
                "continent": self.continent,
                "location": self.location,
                "city": self.city,
                "country_code2": self.country_code2,
                "region": self.region
            }
        }
        return dic

    @staticmethod
    def define_favorite_subjects(number_of_favorite_subjects_distributions, list_of_subjects):
        number_of_subjects = int(round(number_of_favorite_subjects_distributions.rvs(1)[0]))
        subjects = list(np.random.choice(list_of_subjects, number_of_subjects))
        return subjects, len(subjects)

    @staticmethod
    def define_occupations_and_compensation(salary_distribution_per_occupation):
        f = open(static.OCCUPATION)
        data = json.load(f)
        geo_list = []
        for key in data.keys():
            key_list = [key] * data.get(key)
            geo_list += key_list
        occupation = rd.choice(geo_list)
        occupation_normalized = occupation.lower().replace(' ', '_')
        compensation = int(round(salary_distribution_per_occupation[occupation_normalized].rvs(1)[0]))
        modulo = compensation % 100
        compensation = compensation - modulo if compensation < 50 else compensation - modulo + 100
        return occupation, compensation

    def __str__(self):
        return 'firstName: {}, lastName: {}, age: {}, followers: {}'\
            .format(self.firstName, self.lastName, self.age, self.followers)

    @staticmethod
    # Create the users
    def creation_users(yp, distributions_manager, datasets_manager):
        if yp.users is None:
            list_users = []
        else:
            list_users = yp.users
        with open(static.FIRST_NAME) as f:
            first_names = f.read().split('\n')
        with open(static.LAST_NAME) as f:
            last_names = f.read().split('\n')

        peoples = list()
        check = set()

        for i in list_users:
            people = User(distributions_manager, datasets_manager)
            people.firstName, people.lastName = i
            peoples.append(people)
            check.add((people.firstName, people.lastName))
            people.geo_user(yp.localisations)

        for i in range(yp.number_users - len(list_users)):
            people = User(distributions_manager, datasets_manager)
            people.geo_user(yp.localisations)
            people.firstName = first_names[random.randint(0, len(first_names) - 1)]
            people.lastName = last_names[random.randint(0, len(last_names) - 1)]
            while (people.firstName, people.lastName) in check:
                people.lastName = last_names[random.randint(0, len(last_names) - 1)]
            check.add((people.firstName, people.lastName))
            peoples.append(people)

        return peoples

    @staticmethod
    # Create gaussian distribution for the recurrence of messages by user
    def probability_message_user(size):
        s = np.random.normal(static.MU, static.SIGMA, static.SIZE_GAUSSIAN)

        minus = min(s)
        maximum = max(s)

        ratio = (maximum - minus) / size

        probability = [0] * size

        for i in s:
            indices = int(round((maximum - i)/ratio))
            probability[indices - 1] += 1

        total = len(s)

        return [i/total for i in probability]

    def geo_user(self, localisation):
        geo = rd.choice(localisation)
        self.continent = geo[0]
        self.country = geo[1]
        self.region = geo[2]
        self.city = geo[3]
        self.location = {'lon': geo[4], 'lat': geo[5]}
        self.country_code2 = geo[6]

    def message_date_average(self, list_message):
        list_dates = [message.date for message in list_message]
        list_dates.sort(reverse=True)
        delta = list()
        if len(list_dates) <= 1:
            return None
        if len(list_dates) == 2:
            return (list_dates[0] - list_dates[1]).total_seconds()
        for i in range(len(list_dates) - 2):
            delta.append((list_dates[i] - list_dates[i + 1]).total_seconds())

        return sum(delta)/len(delta)
