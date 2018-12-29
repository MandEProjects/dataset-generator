from lib.user import User
from numpy import random
from datetime import datetime, timedelta


class Message:

    def __init__(self):
        self.geo = tuple
        self.city = str()
        self.date = None
        self.text = str()
        self.like = int()
        self.user = User()

    def __str__(self):
        return 'geo: {}, city: {}, date: {}, text: {}, like: {}, lastName: {}, firstName: {}'\
            .format(self.geo, self.city, self.date, self.text, self.like, self.lastName, self.firstName)

    @staticmethod
    # Create the probability from a sample of twitter data
    def prob_message_by_hour():
        total_message_sample = 47508
        # From midnight to 23H59
        numbers_message_sample__by_hour = [2208, 2009, 1917, 1878, 1842, 1531, 1549, 1463,
                                         1192, 1102, 1188, 1132, 1203, 1415, 1497, 1946,
                                         2067, 2215, 2665, 4438, 3358, 2759, 2486, 2448]
        return [i / total_message_sample for i in numbers_message_sample__by_hour]

    def add_date_to_message(self, total_days, date_begin):
        prob = self.prob_message_by_hour()

        random_days = int(random.randint(total_days + 1, size=1)[0])
        random_numbers = int(random.choice(len(prob), 1, p=prob)[0])
        random_minute, random_second = int(random.randint(60, size=1)[0]), int(random.randint(60, size=1)[0])

        date = date_begin + timedelta(days=random_days)
        date = datetime(date.year, date.month, date.day) + timedelta(hours=random_numbers, minutes=random_minute,
                                                                     seconds=random_second)
        return date


