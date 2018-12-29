from lib.yamlParser import YamlParser
from lib.message import Message

yp = YamlParser()

message_list = list()

for i in range(yp.number_messages):
    message = Message()
    message.date = message.add_date_to_message(yp.total_days, yp.date_begin)
    message_list.append(message)


