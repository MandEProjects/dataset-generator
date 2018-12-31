import numpy as np
import random


delta = 5/100
total_message_sample = 47508
# From midnight to 23H59
numbers_message_sample__by_hour = [100, 2009, 1917, 1878, 1842, 1531, 1549, 1463,
                                   1192, 1102, 1188, 1132, 1203, 1415, 1497, 1946,
                                   2067, 2215, 2665, 4438, 3358, 2759, 2486, 2448]
prob = [round(random.uniform(1, -1) * i * delta) for i in numbers_message_sample__by_hour]
total = sum(prob)

new_prob = [i/total for i in prob]
print(sum(new_prob) == 1)
print(total)
print(prob)