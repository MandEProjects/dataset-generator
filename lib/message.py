from lib.user import User
from numpy import random
from datetime import datetime, timedelta
from lib.utilities import get_truncated_normal
import time


class Message:

    def __init__(self):
        self.geo = tuple()
        self.city = str()
        self.date = None
        self.subjects = []
        self.likes = int()
        self.user = None
        self.number_of_subjects = 0

    def __dict__(self):
        dic = {
            "city": self.city,
            "number_of_subjects": self.number_of_subjects,
            "geo": [i for i in self.geo],
            "subjects": self.subjects,
            "like": self.like,
            "date": self.date.isoformat()
        }
        dic.update(self.user.__dict__)
        return dic

    @staticmethod
    # Create the probability from a sample of twitter data
    def prob_message_by_hour(message_distribution, noise):
        message_noise = [i + round(random.uniform(noise, -noise) * i) for i in message_distribution]
        total = sum(message_noise)

        return [i/total for i in message_noise]

    def prob_by_dates(self, total_days, date_begin, message_distribution, noise):
        prob_by_dates = dict()
        for i in range(total_days + 1):
            date = date_begin + timedelta(days=i)
            prob_by_dates.update({date: self.prob_message_by_hour(message_distribution, noise)})
        return prob_by_dates

    @staticmethod
    def add_date_to_message(yp):
        random_days = int(random.randint(yp.total_days + 1, size=1)[0])
        date = yp.beginning_date + timedelta(days=random_days)
        prob = yp.prob_by_dates[date]
        random_numbers = int(random.choice(len(prob), 1, p=prob)[0])
        random_minute, random_second = int(random.randint(60, size=1)[0]), int(random.randint(60, size=1)[0])

        date = yp.beginning_date + timedelta(days=random_days)
        date = datetime(date.year, date.month, date.day) + timedelta(hours=random_numbers, minutes=random_minute,
                                                                     seconds=random_second)
        return date

    def add_subjects_to_message(self, number_of_subjects_distributions, dataset_manager, favorite_user_subjects):
        total_sum = sum(dataset_manager.list_of_subjects_iterations)
        list_of_subject_probabilities = [iteration/total_sum for iteration in
                                         dataset_manager.list_of_subjects_iterations]
        number_of_subjects = int(round(number_of_subjects_distributions.rvs(1)[0]))
        subjects = list(random.choice(dataset_manager.list_of_subjects, number_of_subjects, p=list_of_subject_probabilities))
        self.subjects = subjects
        self.number_of_subjects = len(subjects)

    def add_likes_to_message(self, number_of_likes_distributions):
        self.likes = int(round(number_of_likes_distributions.rvs(1)[0]))





