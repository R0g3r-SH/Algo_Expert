from numpy import sort
from pandas import array


def TowNumber (array,target):
    l = 0
    r = len(array)-1
    array.sort()

    while l<r:
        sum = array[l]+array[r]
        if sum == target:
            return [array[l],array[r]]
        elif sum < target:
            l+=1
        else:
            r=1
    return []




array=[3, 5, -4, 8, 11, 1, -1, 6]
target=10
print(TowNumber(array,target))