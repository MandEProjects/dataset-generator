import json
from scipy.stats import truncnorm
from scipy.stats import truncexpon


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


# Generate bulk to insert in elasticsearch
def generate_bulk(messages):
    # Put json bulk in a file
    with open("outputs/messages.json", "w") as outfile:
        count = 0
        for i in messages:
            outfile.write(json.dumps({"index": {"_index": "test", "_type": "_doc"}}))
            outfile.write("\n")
            outfile.write(json.dumps({"date": i.date.isoformat(),
                                      "subjects": i.subjects,
                                      "number_of_subjects": i.number_of_subjects,
                                      "user": {"name": i.user.firstName + " " + i.user.lastName,
                                               "prob": i.user.probability,
                                               "favorite_subjects": i.user.favorite_subjects,
                                               "number_of_favorite_subjects": i.user.number_of_favorite_subjects,
                                               "age": i.user.age
                                               }}))
            outfile.write("\n")
            count += 1


# Make the function truncnorm more intuitive
# Truncnorm doc: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncnorm.html
def get_truncated_normal(mean, sd, lower_bound, upper_bound):
    return truncnorm((lower_bound - mean) / sd, (upper_bound - mean) / sd, loc=mean, scale=sd)


# Make the function truncexpon more intuitive
# Truncexpon doc: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncexpon.html
def get_truncated_exponential(upper, lower, scale):
    return truncexpon(b=(upper - lower) / scale, loc=lower, scale=scale)


