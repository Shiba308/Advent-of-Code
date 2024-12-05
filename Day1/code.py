import pandas as pd
import numpy as np

csv = pd.read_csv('Day1/input.csv')
data = csv.to_dict()

left = np.array([data['list1'][d] for d in list(data['list1'].keys())])
right = np.array([data['list2'][d] for d in list(data['list2'].keys())])

left_s = np.sort(left)
right_s = np.sort(right)

l_diff = np.abs(right_s - left_s)

answer = np.sum(l_diff)

print(f'Part 1: {answer}')



right_occ = {n:0 for n in set(right)}

for n in right: right_occ[n] = right_occ[n] + 1

sim_score = 0

for num in left:

    if num in right_occ.keys():

        sim_score += num * right_occ[num] 


print(f'Part 2: {sim_score}')



