from lib.message import Message
from lib.distributionsManager import DistributionsManager
import yaml, json
from lib import static, utilities


class YamlParser:

    def __init__(self):
        # Open yaml file
        try:
            yaml_config = yaml.load(open('config/config.yaml'))
        except NameError:
            print('Yaml file not found. Make sure there is a config.yaml in the directory.')
            exit()
        self.beginning_date = self.extract_beginning_date(yaml_config)

        self.total_days, self.number_messages, self.number_users, self.users \
            = self.extract_data_for_message_generation(yaml_config)

        self.favorite_subjects_per_user_distribution, self.favorite_subjects_per_user_mean, \
            self.favorite_subjects_per_user_sd, self.favorite_subjects_per_user_lower_bound, \
            self.favorite_subjects_per_user_upper_bound, self.favorite_subjects_scale = \
            self.extract_data_for_favorites_subjects_per_user_prob(yaml_config)

        self.subjects_distribution, self.subjects_mean, self.subjects_sd, self.subjects_lower_bound, \
            self.subjects_upper_bound, self.subjects_scale = self.extract_data_for_subjects_prob(yaml_config)

        self.age_mean, self.age_sd, self.age_lower_bound, self.age_upper_bound \
            = self.extract_data_age_prob(yaml_config)

        self.likes_upper_bound, self.likes_lower_bound, self.likes_scale = self.extract_data_likes_prob(yaml_config)

        self.followers_upper_bound, self.followers_lower_bound, self.followers_scale = self.extract_data_followers_prob(yaml_config)

        self.compensations_distribution = self.extract_compensations_prob(yaml_config)

        self.message_distribution, self.granularity, self.noise = self.message_distribution(yaml_config)

        self.prob_message_by_hour = Message.prob_message_by_hour(self.message_distribution, self.noise)

        self.prob_by_dates = Message().prob_by_dates(self.total_days, self.beginning_date,
                                                     self.message_distribution, self.noise)

        self.index_name, self.index, self.override = self.index_elasticsearch(yaml_config)

        self.localisations = self.localisation_messages()

    @staticmethod
    def localisation_messages():

        f = open(static.LOCALISATION)
        data = json.load(f)
        geo_list = []
        for key in data.keys():
            key_list = [eval(key)] #* data.get(key)
            geo_list += key_list

        return geo_list

    @staticmethod
    def index_elasticsearch(yaml_config):
        index_name = static.INDEX_NAME if yaml_config['index_name'] is None else yaml_config['index_name']
        index = bool(True if yaml_config['index'] is None else yaml_config['index'])
        override = bool(True if yaml_config['override'] is None else yaml_config['override'])
        return index_name, index, override

    @staticmethod
    def message_distribution(yaml_config):
        f = open(yaml_config['message_generation']['path'])
        granularity = yaml_config['message_generation']['granularity']
        noise = yaml_config['message_generation']['noise']

        for i in f:
            numbers = [int(x) for x in i.replace('[', '').replace(']', '').split(',')]

        utilities.check_message_distribution(noise, granularity, numbers)

        return numbers, granularity, noise


    @staticmethod
    def extract_beginning_date(yaml_config):
        try:
            return yaml_config.get(static.DATE)
        except TypeError:
            print("The date as to be like YYYY-MM-DD.")
            exit()

    @staticmethod
    def extract_data_for_message_generation(yaml_config):
        try:
            total_days = yaml_config.get(static.DAYS)
            number_messages = yaml_config.get(static.MESSAGE_NUMBER)
            number_users = yaml_config.get(static.NUMBER_USER)
            users = yaml_config.get(static.NAMES)
            if users is None:
                users = []
            return total_days, number_messages, number_users, users
        except:
            print("Incorrect configuration file")
            exit()

    @staticmethod
    def extract_data_for_favorites_subjects_per_user_prob(yaml_config):
        try:
            distribution = static.favorites_subjects_type(yaml_config)
            if distribution not in static.DISTRIBUTION_FAVORITE_SUBJECTS_PER_USER:
                print("Incorrect distribution type for the favorite_subjects_per_user_distribution")
                exit(422)
            mean = static.favorites_subjects_params(yaml_config, static.MEAN)
            sd = static.favorites_subjects_params(yaml_config, static.SD)
            upper_bound = static.favorites_subjects_params(yaml_config, static.UPPER_BOUND)
            lower_bound = static.favorites_subjects_params(yaml_config, static.LOWER_BOUND)
            scale = static.favorites_subjects_params(yaml_config, static.SCALE)
            if distribution is static.NORMAL:
                return utilities.preparation_return((distribution, mean, sd, lower_bound, upper_bound, None))
            else:
                return utilities.preparation_return((distribution, None, None, lower_bound, upper_bound, scale))
        except:
            if distribution is None or distribution is static.NORMAL:
                return static.NORMAL_DISTRIBUTION
            else:
                return static.EXPONENTIAL_DISTRIBUTION

    @staticmethod
    def extract_data_for_subjects_prob(yaml_config):
        try:
            distribution = static.subjects_distribution_type(yaml_config)
            if distribution not in static.DISTRIBUTION_SUBJECTS:
                print("Incorrect distribution type for the favorite_subjects_per_user_distribution")
                exit(422)
            mean = static.subjects_distribution_params(yaml_config, static.MEAN)
            sd = static.subjects_distribution_params(yaml_config, static.SD)
            upper_bound = static.subjects_distribution_params(yaml_config, static.UPPER_BOUND)
            lower_bound = static.subjects_distribution_params(yaml_config, static.LOWER_BOUND)
            scale = static.subjects_distribution_params(yaml_config, static.SCALE)
            if distribution is static.NORMAL:
                return utilities.preparation_return((distribution, mean, sd, lower_bound, upper_bound, None))
            else:
                return utilities.preparation_return((distribution, None, None, lower_bound, upper_bound, scale))
        except:
            if distribution is None or distribution is static.NORMAL:
                return static.NORMAL_DISTRIBUTION
            else:
                return static.EXPONENTIAL_DISTRIBUTION

    @staticmethod
    def extract_data_age_prob(yaml_config):
        try:
            mean = static.age_distribution(yaml_config, static.MEAN)
            sd = static.age_distribution(yaml_config, static.SD)
            upper_bound = static.age_distribution(yaml_config, static.UPPER_BOUND)
            lower_bound = static.age_distribution(yaml_config, static.LOWER_BOUND)
            return utilities.preparation_age_return((mean, sd, lower_bound, upper_bound))
        except:
            print('error')
            return static.AGE_DISTRIBUTION

    @staticmethod
    def extract_data_likes_prob(yaml_config):
        try:
            upper_bound = static.likes_distribution(yaml_config, static.UPPER_BOUND)
            lower_bound = static.likes_distribution(yaml_config, static.LOWER_BOUND)
            scale = static.likes_distribution(yaml_config, static.SCALE)
            return utilities.preparation_likes_return((upper_bound, lower_bound, scale))
        except:
            print('error')
            return static.LIKES_DISTRIBUTION

    @staticmethod
    def extract_compensations_prob(yaml_config):
        with open(yaml_config['message_generation']['user_occupation']) as f:
            occupations = json.load(f)
        compensations_prob = {}
        for occupation in occupations:
            occupation_normalized = occupation.lower().replace(' ', '_')
            try:
                mean = static.compensation_distribution(yaml_config, occupation_normalized, static.MEAN)
                sd = static.compensation_distribution(yaml_config, occupation_normalized, static.SD)
                upper_bound = static.compensation_distribution(yaml_config, occupation_normalized, static.UPPER_BOUND)
                lower_bound = static.compensation_distribution(yaml_config, occupation_normalized, static.LOWER_BOUND)
                compensations_prob[occupation_normalized] = utilities.preparation_compensation_return((mean, sd, lower_bound, upper_bound))
            except:
                print('error')
                compensations_prob[occupation_normalized] = static.COMPENSATION_DISTRIBUTION
        return compensations_prob

    @staticmethod
    def extract_data_followers_prob(yaml_config):
        try:
            upper_bound = static.follower_distribution(yaml_config, static.UPPER_BOUND)
            lower_bound = static.follower_distribution(yaml_config, static.LOWER_BOUND)
            scale = static.follower_distribution(yaml_config, static.SCALE)
            return utilities.preparation_followers_return((upper_bound, lower_bound, scale))
        except:
            print('error')
            return static.FOLLOWERS_DISTRIBUTION