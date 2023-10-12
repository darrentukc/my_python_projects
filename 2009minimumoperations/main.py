import pandas as pd

continuous = False
counter = 0
list_of_nums = [1,10,100,1000]


if len(list_of_nums) == len(set(list_of_nums)):
    if (max(list_of_nums) - min(list_of_nums)) == (len(list_of_nums) - 1):
        continuous = True
        print(counter)

if not continuous:
    for index in range(len(list_of_nums)):
        if (index + 1) not in list_of_nums:
            counter += 1
    print(counter)