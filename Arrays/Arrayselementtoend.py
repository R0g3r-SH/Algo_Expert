def moveElementToEnd(array, toMove):
    # Write your code here.
    l = 0
    r = 0
    while r<len(array):
        lval= array[l]
        rval = array[r]
        if lval == toMove and rval  == toMove:
            r+=1
            continue
        if lval == toMove and rval  != toMove:
            array[l],array[r] = array[r] , array[l]
            l+=1
            r+=1   
            continue
        if lval != toMove and rval  != toMove:
            l+=1
            r+=1
            continue
    return array


array= [2, 1, 2, 2, 2, 3, 4, 2]
toMove= 2
print(moveElementToEnd(array,toMove))