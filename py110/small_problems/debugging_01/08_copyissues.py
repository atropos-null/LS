""" Problem: original is a list of lists, therefore the original use of copy only creates a shallow copy, 
where the nested lists are still references to the original lists. Therefore, a change to the copy reflects 
a change in the original list. copy.deepcopy() is required."""

import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)
original[0][0] = 99

print(copied[0] == [1])