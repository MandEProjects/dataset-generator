from lib.utilities import get_truncated_normal

"""
import requests
import json

json_tags = {}
for page in range(1, 31):
    response = requests.get("https://api.stackexchange.com/2.2/tags?{0}&{1}&order=desc&sort=popular&site=stackoverflow"
        .format("page="+str(page), "pagesize=100"))
    json_response = response.json()
    for tag in json_response["items"]:
        if tag["count"] > 100000:
            json_tags[tag["name"]] = int(tag["count"]/10)
        else:
            json_tags[tag["name"]] = tag["count"]


json_tags["elasticstack"] = 250678
json_tags["elasticsearch"] = 221543
json_tags["kibana"] = 214767
json_tags["logstash"] = 204783
json_tags["beats"] = 191745
json_tags["metricbeat"] = 56976
json_tags["packetbeat"] = 53908
json_tags["auditbeat"] = 51890
json_tags["heartbeat"] = 50930
json_tags["filebeat"] = 54096
json_tags["functionbeat"] = 48765

with open("hashtags.json", "w") as outfile:
    outfile.write(json.dumps(json_tags))
"""


X0 = get_truncated_normal(mean=2, sd=0.5, low=1, upp=5)
X1 = get_truncated_normal(mean=2, sd=1, low=1, upp=5)
X2 = get_truncated_normal(mean=3., sd=1, low=1, upp=5)
X3 = get_truncated_normal(mean=4, sd=1, low=1, upp=5)

print(X1.rvs(1))

import matplotlib.pyplot as plt
fig, ax = plt.subplots(4, sharex=True)
ax[0].hist(X0.rvs(10000))
ax[1].hist(X1.rvs(10000))
ax[2].hist(X2.rvs(10000))
ax[3].hist(X3.rvs(10000))
plt.show()