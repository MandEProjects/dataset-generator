import json


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
def generate_bulk(json_list):
    # Put json bulk in a file
    with open("hashtags.json", "w") as outfile:
        count = 0
        for i in json_list:
            outfile.write(json.dumps({"index": {"_index": "test", "_type": "_doc", "_id": count}}))
            outfile.write("\n")
            outfile.write(json.dumps({"date": i.isoformat()}))
            outfile.write("\n")
            count += 1



