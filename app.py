from lib.yamlParser import YamlParser
from lib.message import Message
from lib.user import User
from lib import utilities
from numpy import random
import time

t1 = time.time()
yp = YamlParser()

message_list = list()

list_users = User.creation_users(yp.number_users, yp.users)
prob_users = User.probability_message_user(yp.number_users)

for i in range(yp.number_messages):
    message = Message()
    message.date = message.add_date_to_message(yp.total_days, yp.date_begin)
    indices = int(random.choice(len(prob_users), 1, p=prob_users)[0])
    user = list_users[indices]
    user.probability = prob_users[indices]
    message.user = user
    message_list.append(message)

utilities.generate_bulk(message_list)
print(time.time() - t1)
