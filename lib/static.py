# Path static

LOCALISATION = "datasets/data.json"
FIRST_NAME = 'datasets/firstName.txt'
LAST_NAME = 'datasets/lastName.txt'


# mean and standard deviation for probability_message_user
MU = 0
SIGMA = 0.5
SIZE_GAUSSIAN = 1000000


# probability that the localisation of the message will be the localisation of the user
PROBABILITY_MESSAGE_USER_LOCALISATION = 0.6


# Distribution manager
DATE = 'date'
DAYS = 'days'
MESSAGE_NUMBER = 'message_number'
NUMBER_USER = 'number_user'
NAMES = 'names'
NORMAL = 'normal'
EXPONENTIAL = 'exponential'
SCALE = 'scale'
LOWER_BOUND = 'lower_bound'
UPPER_BOUND = 'upper_bound'
SD = 'sd'
MEAN = 'mean'
NOISE = 0.25

DISTRIBUTION_FAVORITE_SUBJECTS_PER_USER = [EXPONENTIAL, NORMAL]
DISTRIBUTION_SUBJECTS = [EXPONENTIAL, NORMAL]

# name function - mean - sd - lower_bound - upper_bound - scale
NORMAL_DISTRIBUTION = (NORMAL, 4.8, 1.2, 1, 7, None)

# name function - mean - sd - lower_bound - upper_bound - scale
EXPONENTIAL_DISTRIBUTION = (EXPONENTIAL, None, None, 1, 10, 2)

# mean - sd - lower_bound - upper_bound
AGE_DISTRIBUTION = (37, 6, 20, 60)
COMPENSATION_DISTRIBUTION = (100000, 5000, 80000, 120000)

# upper_bound, lower_bound, scale
LIKES_DISTRIBUTION = (1000, 0, 180)

# upper_bound, lower_bound, scale
FOLLOWERS_DISTRIBUTION = (3000, 0, 500)


# Yaml parser
def favorites_subjects_type(yaml):
    return yaml.get("distributions").get("favorite_subjects_per_user_distribution").get("type")


def favorites_subjects_params(yaml, string):
    return yaml.get("distributions").get("favorite_subjects_per_user_distribution").get("params").get(string)


def subjects_distribution_type(yaml):
    return yaml.get("distributions").get("subjects_distribution").get("type")


def subjects_distribution_params(yaml, string):
    return yaml.get("distributions").get("subjects_distribution").get("params").get(string)


def age_distribution(yaml, string):
    return yaml.get("distributions").get("age_distribution").get("params").get(string)


def compensation_distribution(yaml, occupation, string):
    return yaml.get("distributions").get("compensation").get(occupation).get("params").get(string)


def likes_distribution(yaml, string):
    return yaml.get("distributions").get("likes_distribution").get("params").get(string)


def follower_distribution(yaml, string):
    return yaml.get("distributions").get("followers_distribution").get("params").get(string)


