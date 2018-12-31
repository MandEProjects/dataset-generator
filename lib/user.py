import random
import numpy as np
import matplotlib.pyplot as plt
from lib import utilities


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
        with open("datasets/firstName.txt") as f:
            first_names = f.read().split('\n')
        with open("datasets/lastName.txt") as f:
            last_names = f.read().split('\n')

        peoples = list()
        check = set()

        for i in list_users:
            pple = User(distributions_manager, datasets_manager)
            pple.firstName, pple.lastName = i
            peoples.append(pple)
            check.add((pple.firstName, pple.lastName))

        for i in range(yp.number_users - len(list_users)):
            pple = User(distributions_manager, datasets_manager)
            pple.firstName = first_names[random.randint(0, len(first_names) - 1)]
            pple.lastName = last_names[random.randint(0, len(last_names) - 1)]
            while (pple.firstName, pple.lastName) in check:
                pple.lastName = last_names[random.randint(0, len(last_names) - 1)]
            check.add((pple.firstName, pple.lastName))
            peoples.append(pple)

        return peoples

    @staticmethod
    # Create gaussian distribution for the recurrence of messages by user
    def probability_message_user(size):
        mu, sigma = 0, 0.5  # mean and standard deviation
        s = np.random.normal(mu, sigma, 1000000)

        minus = min(s)
        maximum = max(s)

        ratio = (maximum - minus) / size

        probability = [0] * size

        for i in s:
            indices = int(round((maximum - i)/ratio))
            probability[indices - 1] += 1

        total = len(s)

        return [i/total for i in probability]


# count, bins, ignored = plt.hist(s, 100, density=True)
