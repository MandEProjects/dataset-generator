import yaml
from lib.yamlParser import YamlParser
from lib.message import Message
from lib.user import User

# Open yaml file
try:
    yaml_config = yaml.load(open('config.yaml'))
except NameError:
    print('Yaml file not found. Make sure there is a config.yaml in the directory.')
    exit()

yp = YamlParser(yaml_config)

message_list = list()

print(len(User.creation_users(yp.number_users, yp.users)))

for i in range(yp.number_messages):
    message = Message()
    message.date = message.add_date_to_message(yp.total_days, yp.date_begin)
    message_list.append(message)


