from lib.yamlParser import YamlParser
from lib.message import Message
from lib.user import User
from lib import utilities
from numpy import random
from lib.datasetsManager import DatasetsManager
from lib.distributionsManager import DistributionsManager

import time

t1 = time.time()
yp = YamlParser()
datasets_manager = DatasetsManager()
distributions_manager = DistributionsManager(yaml_parser=yp)

message_list = list()

list_users = User.creation_users(yp, distributions_manager, datasets_manager)
prob_users = User.probability_message_user(yp.number_users)

prob = Message.prob_message_by_hour()
for i in range(yp.number_messages):
    message = Message()
    message.date = message.add_date_to_message(yp)
    indices = int(random.choice(len(prob_users), 1, p=prob_users)[0])
    user = list_users[indices]
    user.probability = prob_users[indices]
    message.user = user
    message.add_subjects_to_message(distributions_manager.subjects_distribution, datasets_manager, user.favorite_subjects)
    message_list.append(message)

utilities.generate_bulk(message_list)
print("Program took: {0}".format(time.time() - t1))
