import yaml

yp = yaml.load(open('config/config.yaml'))
f = open(yp.get('message_generation').get('path'))

for i in f:
    numbers = [int(x) for x in i.replace('[','').replace(']','').split(',')]
print(numbers)
