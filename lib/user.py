import random
import numpy as np
import matplotlib.pyplot as plt
from lib import utilities
from lib import static


class User:

    def __init__(self, distributions_manager, datasets_manager):
        self.lastName = str()
        self.firstName = str()
        self.age = int(round(distributions_manager.age_distribution.rvs(1)[0]))
        self.followers = int()
        self.probability = int()
        self.favorite_subjects, self.number_of_favorite_subjects = self.define_favorite_subjects(
            distributions_manager.favorite_subjects_per_user_distribution, datasets_manager.list_of_subjects)

    @staticmethod
    def define_favorite_subjects(number_of_favorite_subjects_distributions, list_of_subjects):
        number_of_subjects = int(round(number_of_favorite_subjects_distributions.rvs(1)[0]))
        subjects = list(np.random.choice(list_of_subjects, number_of_subjects))
        return subjects, len(subjects)

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

        for i in range(yp.number_users - len(list_users)):
            people = User(distributions_manager, datasets_manager)
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

