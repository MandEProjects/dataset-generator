import random
import numpy as np
import matplotlib.pyplot as plt
from lib import utilities


class User:

    def __init__(self):
        self.lastName = str()
        self.firstName = str()
        self.age = int()
        self.followers = int()
        self.probability = int()

    def __str__(self):
        return 'firstName: {}, lastName: {}, age: {}, followers: {}'\
            .format(self.firstName, self.lastName, self.age, self.followers)

    @staticmethod
    # Create the users
    def creation_users(nbr_users, list_users=[]):
        with open("datasets/firstName.txt") as f:
            first_names = f.read().split('\n')
        with open("datasets/lastName.txt") as f:
            last_names = f.read().split('\n')

        peoples = list()
        check = set()

        for i in list_users:
            pple = User()
            pple.firstName, pple.lastName = i
            peoples.append(pple)
            check.add((pple.firstName, pple.lastName))

        for i in range(nbr_users - len(list_users)):
            pple = User()
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

        ratio = (max(s) - min(s))/size
        minus = min(s)
        last_number = True
        list_active = []
        count = 0
        for i in sorted(s):
            if i <= minus + ratio:
                count += 1
                last_number = False
            else:
                while i > minus + ratio:
                    minus += ratio
                    list_active.append(count)
                    count = 0
                count = 1
                last_number = True

        if len(list_active) < size:
            list_active.append(count)
        elif last_number:
            list_active[len(list_active) - 1] += 1

        total = len(s)

        return [i/total for i in list_active]


# count, bins, ignored = plt.hist(s, 100, density=True)
