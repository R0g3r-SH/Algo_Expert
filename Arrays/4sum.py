from pandas import array


def fourNumberSum(array, targetSum):
    # Write your code here.
    ptr = 1
    cuadluplets = []
    hashtable = {}
    while ptr < len(array):
        r = ptr+1
        #rigth
        while r <= len(array)-1:
            sum = array[ptr]+array[r]
            target2 = targetSum-sum
            if target2 in hashtable:
                for val in hashtable[target2]:
                    cuadluplets.append(val+[array[ptr],array[r]])
            r+=1
        l = 0
        while l <ptr:
            sum = array[ptr]+array[l]
            if sum in hashtable:
                hashtable[sum].append([array[ptr],array[l]])
                
            else:
                hashtable[sum] = [[array[ptr],array[l]]]
            l+=1
        ptr+=1
    return cuadluplets

targetSum  =16
array =[7, 6, 4, -1, 1, 2]
print(fourNumberSum(array, targetSum))