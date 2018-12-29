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
