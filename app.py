from lib.yamlParser import YamlParser
from lib.message import Message
from lib.user import User
from lib import output, utilities
from numpy import random
from lib.datasetsManager import DatasetsManager
from lib.distributionsManager import DistributionsManager
import time,json

t1 = time.time()
yp = YamlParser()
datasets_manager = DatasetsManager()
distributions_manager = DistributionsManager(yaml_parser=yp)

message_list = list()

list_users = User.creation_users(yp, distributions_manager, datasets_manager)
prob_users = User.probability_message_user(yp.number_users)

for i in range(yp.number_messages):
    message = Message()
    message.add_date_to_message(yp)
    indices = int(random.choice(len(prob_users), 1, p=prob_users)[0])
    user = list_users[indices]
    user.probability = prob_users[indices]
    message.user = user
    message.add_subjects_to_message(distributions_manager.subjects_distribution, datasets_manager, user.favorite_subjects)
    message.add_likes_to_message(user, distributions_manager.build_likes_distribution(yp))
    message.add_geo_to_message(yp, user)
    message_list.append(message)

print("Message generation is done")
print("Indexing the messages")

print(yp.index)
if not yp.index:
    utilities.generate_bulk(message_list)
else:
    if yp.override:
        output.override(yp.index_name)
    json_list = []
    for message in message_list:
        try:
            json_list.append(message.__dict__())
        except:
            print("Error with dict message")
            exit()
    output.insert_elasticsearch(json_list, yp.index_name)


print("Program took: {0}".format(time.time() - t1))

