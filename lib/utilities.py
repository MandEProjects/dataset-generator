import json
from scipy.stats import truncnorm
from scipy.stats import truncexpon
from lib import static


# This function count the recurrence of term in a list a print ordered dict.
def list_repartition(a_list):
    repartition = dict()
    for i in a_list:
        string = str(i)
        if repartition.get(string) is None:
            repartition.update({string: 1})
        else:
            repartition.update({string: repartition[string] + 1})
    for key in sorted(repartition.keys()):
        print("%s: %s" % (key, repartition[key]))


# Make the function truncnorm more intuitive
# Truncnorm doc: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncnorm.html
def get_truncated_normal(mean, sd, lower_bound, upper_bound, loc=None):
    if loc is None:
        loc = mean
    return truncnorm((lower_bound - mean) / sd, (upper_bound - mean) / sd, loc=loc, scale=sd)


# Make the function truncexpon more intuitive
# Truncexpon doc: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncexpon.html
def get_truncated_exponential(upper, lower, scale):
    return truncexpon(b=(upper - lower) / scale, loc=lower, scale=scale)


# Return default value normal & expo
def preparation_return(tuple_test):
    print(tuple_test)
    if tuple_test[0] is static.NORMAL:
        distribution = static.NORMAL_DISTRIBUTION
    else:
        distribution = static.EXPONENTIAL_DISTRIBUTION
    tuple_return = list()
    for i in range(len(tuple_test)):
        tuple_return.append(tuple_test[i] if tuple_test[i] is not None else distribution[i])
    return tuple(tuple_return)


# Return age
def preparation_age_return(tuple_test):
    tuple_return = list()
    for i in range(len(tuple_test)):
        tuple_return.append(tuple_test[i] if tuple_test[i] is not None else static.AGE_DISTRIBUTION[i])
    return tuple(tuple_return)


# Return compensation
def preparation_compensation_return(tuple_test):
    tuple_return = list()
    for i in range(len(tuple_test)):
        tuple_return.append(tuple_test[i] if tuple_test[i] is not None else static.COMPENSATION_DISTRIBUTION[i])
    return tuple(tuple_return)


# Return likes
def preparation_likes_return(tuple_test):
    tuple_return = list()
    for i in range(len(tuple_test)):
        tuple_return.append(tuple_test[i] if tuple_test[i] is not None else static.LIKES_DISTRIBUTION[i])
    return tuple(tuple_return)


# Return likes
def preparation_followers_return(tuple_test):
    tuple_return = list()
    for i in range(len(tuple_test)):
        tuple_return.append(tuple_test[i] if tuple_test[i] is not None else static.FOLLOWERS_DISTRIBUTION[i])
    return tuple(tuple_return)


def check_message_distribution(noise, granularity, message_distribution):
    if granularity is 'h' and len(message_distribution) != 24:
        print('You should have 24 values in your message_distribution.txt.')
        exit()
    if granularity is 'm' and len(message_distribution) != 1440:
        print('You should have 1440 values in your message_distribution.txt.')
        exit()
    if not (0 <= noise <= 1):
        print('Your noise should be between 0 to 1.')
        exit()


