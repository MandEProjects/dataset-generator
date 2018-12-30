from lib.message import Message
from lib.distributionsManager import DistributionsManager
import yaml


class YamlParser:

    DISTRIBUTION_NUMBER_OF_SUBJECTS_PER_USER = ["exponential", "normal"]
    UPPER_BOUND_NUMBER_OF_SUBJECTS_PER_USER = 7

    def __init__(self):
        # Open yaml file
        try:
            yaml_config = yaml.load(open('config/config.yaml'))
        except NameError:
            print('Yaml file not found. Make sure there is a config.yaml in the directory.')
            exit()
        self.begining_date = self.extract_beginning_date(yaml_config)
        self.total_days, self.number_messages, self.number_users, self.users \
            = self.extract_data_for_message_generation(yaml_config)
        self.number_of_subjects_per_user_distribution, \
            self.number_of_subjects_per_user_mean,\
            self.number_of_subjects_per_user_sd, \
            self.number_of_subjects_per_user_lower_bound, \
            self.number_of_subjects_per_user_upper_bound \
            = self.extract_data_for_number_of_subjects_per_user_prob(yaml_config)
        self.prob_message_by_hour = Message.prob_message_by_hour()

    @staticmethod
    def extract_beginning_date(yaml_config):
        try:
            return yaml_config.get('date')
        except TypeError:
            print("The date as to be like YYYY-MM-DD.")
            exit()

    @staticmethod
    def extract_data_for_message_generation(yaml_config):
        try:
            total_days = yaml_config.get('days')
            number_messages = yaml_config.get('tweet_number')
            number_users = yaml_config.get('number_user')
            if yaml_config.get('names') is None:
                users = []
            users = yaml_config.get('names')
            return total_days, number_messages, number_users, users
        except:
            print("Incorrect configuration file")
            exit()

    def extract_data_for_number_of_subjects_per_user_prob(self, yaml_config):
        try:
            distribution = yaml_config.get("distributions")\
                    .get("number_of_subjects_per_user_distribution")\
                    .get("type")
            if distribution not in self.DISTRIBUTION_NUMBER_OF_SUBJECTS_PER_USER:
                print("Incorrect distribution type for the number_of_subjects_per_user_distribution")
                exit(422)
            mean = yaml_config.get("distributions") \
                .get("number_of_subjects_per_user_distribution") \
                .get("params") \
                .get("mean")
            sd = yaml_config.get("distributions") \
                .get("number_of_subjects_per_user_distribution") \
                .get("params") \
                .get("sd")
            upper_bound = yaml_config.get("distributions") \
                .get("number_of_subjects_per_user_distribution") \
                .get("params") \
                .get("upper_bound")
            lower_bound = yaml_config.get("distributions") \
                .get("number_of_subjects_per_user_distribution") \
                .get("params") \
                .get("lower_bound")
            return distribution, mean, sd, lower_bound, upper_bound
        except:
            return None, None, None, None, None

