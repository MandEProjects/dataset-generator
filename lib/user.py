import random


class User:

    def __init__(self):
        self.lastName = str()
        self.firstName = str()
        self.age = int()
        self.followers = int()

    def __str__(self):
        return 'firstName: {}, lastName: {}, age: {}, followers: {}'\
            .format(self.firstName, self.lastName, self.age, self.followers)

    @staticmethod
    # Create the users
    def creation_users(nbr_users, list_users=[]):
        with open("datasets/firstName.txt") as f:
            first_names = f.readlines()
        with open("datasets/lastName.txt") as f:
            last_names = f.readlines()

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
