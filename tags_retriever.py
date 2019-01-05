from lib.utilities import get_truncated_normal, get_truncated_exponential

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
import scipy.stats as stats
import matplotlib.pyplot as plt

lower, upper, scale = 1, 10, 1
X4 = stats.truncexpon(b=(upper-lower)/scale, loc=lower, scale=scale)
lower, upper, scale = 1, 10, 2
X5 = stats.truncexpon(b=(upper-lower)/scale, loc=lower, scale=scale)
lower, upper, scale = 1, 10, 1.6
X6 = stats.truncexpon(b=(upper-lower)/scale, loc=lower, scale=scale)


X0 = get_truncated_normal(mean=2, sd=0.5, lower_bound=1, upper_bound=7)
X1 = get_truncated_normal(mean=2, sd=1.5, lower_bound=1, upper_bound=7)
X2 = get_truncated_normal(mean=3.5, sd=1.0, lower_bound=1, upper_bound=7)
X4 = get_truncated_normal(mean=27, sd=6, lower_bound=20, upper_bound=60, loc=40)
X5 = get_truncated_normal(mean=37, sd=6, lower_bound=20, upper_bound=60)
X6 = get_truncated_normal(mean=37, sd=6, lower_bound=20, upper_bound=60, loc=20)

print(X1.rvs(1))

import matplotlib.pyplot as plt
fig, ax = plt.subplots(3, sharex=True)
#ax[0].hist(X0.rvs(500000))
#ax[1].hist(X1.rvs(500000))
#ax[2].hist(X2.rvs(500000))
#ax[3].hist(X3.rvs(500000))
ax[0].hist(X4.rvs(200000))
ax[1].hist(X5.rvs(200000))
ax[2].hist(X6.rvs(200000))
plt.show()



#load libraries
import scipy.stats as stats

#lower, upper, mu, and sigma are four parameters
lower, upper = 0, 400000
mu, sigma = 170000, 50000

#instantiate an object X using the above four parameters,
X = stats.truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)

#generate 1000 sample data
samples = X.rvs(10000)

#make a histogram for the samples
plt.hist(samples, bins= 100,alpha=0.3,label='histogram');


#legend
plt.legend(loc='best')

plt.show()