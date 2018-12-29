from datetime import datetime


class Tweet:

    def __init__(self):
        self.geo = tuple
        self.city = str()
        self.date = None
        self.text = str()
        self.like = int()
        self.lastName = str()
        self.firstName = str()

    def __str__(self):
        return 'geo: {}, city: {}, date: {}, text: {}, like: {}, lastName: {}, firstName: {}'\
            .format(self.geo, self.city, self.date, self.text, self.like, self.lastName, self.firstName)

