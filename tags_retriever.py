from lib.utilities import get_truncated_normal, get_truncated_exponential
import requests
import json

from bs4 import BeautifulSoup


with open("datasets/subjects.json") as f:
    data = json.load(f)


print(len(data))


URL = "https://top-hashtags.com/instagram/{0}/"

hashtags = []
for i in range(1, 3201, 100):
    response = requests.get(URL.format(i))
    print(URL.format(i))
    result = response.content
    soup = BeautifulSoup(result, 'html.parser')
    res = soup.find_all("div", class_="tht-tag small-7 medium-9 columns")
    for hashtag in res:
        hashtags.append(hashtag.find("a").text)


new_dataset = {}
for counter, i in enumerate(data):
    print(counter, i)
    new_dataset[hashtags[counter]] = data[i]


print(new_dataset)
print(len(new_dataset))

with open("datasets/subjects.json", "w") as outfile:
    outfile.write(json.dumps(new_dataset))