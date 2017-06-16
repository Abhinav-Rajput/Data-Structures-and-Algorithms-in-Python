# In Code Fragment 5.1, we perform an experiment to compare the length of
# a Python list to its underlying memory usage. Determining the sequence
# of array sizes requires a manual inspection of the output of that program.
# Redesign the experiment so that the program outputs only those values of
# k at which the existing capacity is exhausted. For example, on a system
# consistent with the results of Code Fragment 5.2, your program should
# output that the sequence of array capacities are 0, 4, 8, 16, 25, . . . .

import sys
data = []
cur = 0
for k in range(30):
    a = len(data)
    b = sys.getsizeof(data)
    if b > cur and a > 0:
        cur = b
        print('''Exausted when lenth = {0}'''.format(a - 1))
    data.append(None)
