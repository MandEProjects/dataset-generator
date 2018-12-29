class People:

    def __init__(self):
        self.lastName = str()
        self.firstName = str()
        self.age = int()
        self.followers = int()

    def __str__(self):
        return 'firstName: {}, lastName: {}, age: {}, followers: {}'\
            .format(self.firstName, self.lastName, self.age, self.followers)
