import json
from scipy.stats import truncnorm


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
            outfile.write(json.dumps({"index": {"_index": "test", "_type": "_doc", "_id": count}}))
            outfile.write("\n")
            outfile.write(json.dumps({"date": i.date.isoformat(),
                                      "user": {"firstName": i.user.firstName, "lastName": i.user.lastName, "prob": i.user.probability}}))
            outfile.write("\n")
            count += 1


# Make the function truncnorm more intuitive
# Truncnorm doc: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncnorm.html
def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


