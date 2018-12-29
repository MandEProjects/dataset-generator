import yaml
from lib.generateTweet import GenerateTweet

# Open yaml file
try:
    yaml_config = yaml.load(open('config.yaml'))
except NameError:
    print('Yaml file not found. Make sure there is a config.yaml in the directory.')
    exit()

gt = GenerateTweet(yaml_config)
gt.generate_tweet()


