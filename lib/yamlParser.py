from lib.message import Message
import yaml


class YamlParser:
    def __init__(self):
        # Open yaml file
        try:
            yaml_config = yaml.load(open('config/config.yaml'))
        except NameError:
            print('Yaml file not found. Make sure there is a config.yaml in the directory.')
            exit()
        try:
            self.date_begin = yaml_config.get('date')
        except TypeError:
            print("The date as to be like 2018-10-08.")
            exit()
        try:
            self.total_days = yaml_config.get('days')
            self.number_messages = yaml_config.get('tweet_number')
            self.number_users = yaml_config.get('number_user')
            if yaml_config.get('names') is None:
                self.users = []
            self.users = yaml_config.get('names')
        except:
            print("Verify your yaml file")
            exit()
        self.prob_message_by_hour = Message.prob_message_by_hour()




