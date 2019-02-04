from lib.yamlParser import YamlParser
from lib.message import Message
from lib.user import User
from lib import output, utilities
from numpy import random
from lib.datasetsManager import DatasetsManager
from lib.distributionsManager import DistributionsManager
import time

t0 = time.time()
t1 = time.time()

yp = YamlParser()
datasets_manager = DatasetsManager()
distributions_manager = DistributionsManager(yaml_parser=yp)

print("Creation Yamel parser : {}s".format(time.time() - t1))
t1 = time.time()

message_list = list()

list_users = User.creation_users(yp, distributions_manager, datasets_manager)
prob_users = User.probability_message_user(yp.number_users)

print("Creation of the users : {}s".format(time.time() - t1))
t1 = time.time()

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

print("Message generates: {}s".format(time.time() - t1))
t1 = time.time()

json_list_message = []
for message in message_list:
    try:
        json_list_message.append(message.__dict__())
    except:
        print("Error with dict message")
        exit()

json_list_user = []
for user in list_users:
    list_message_user = [message for message in message_list if message.user.id == user.id]
    json_list_user.append(user.elastic_mapping_user_centric(list_message_user))
print("All users created : {}s".format(time.time() - t1))
t1 = time.time()

if yp.bulk:
    output.generate_bulk(json_list_user, yp.index_user, yp.doc_type)
    output.generate_bulk(json_list_message, yp.index_message, yp.doc_type)

if yp.index:
    if yp.override:
        output.override_user(yp.index_user)
        output.override_message(yp.index_message)
        print("Overide indexes : {}s".format(time.time() - t1))
        t1 = time.time()

    output.insert_elasticsearch(json_list_message, yp.index_message, yp.doc_type)
    print("Messages inserted in elastic: {}s".format(time.time() - t1))
    t1 = time.time()
    output.insert_elasticsearch(json_list_user, yp.index_user, yp.doc_type)
    print("User index inserted in elastic : {}s".format(time.time() - t1))
print("Program took: {0}".format(time.time() - t0))


