from lib.utilities import get_truncated_normal


class DistributionsManager:

    def __init__(self):
            self.number_of_subjects_distribution = get_truncated_normal(mean=4.8, sd=1.2, lower_bound=1, upper_bound=7)