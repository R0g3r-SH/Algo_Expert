def sortedSquaredArray(array):
    # Write your code here.
    new=[0]*len(array)
    l = 0 
    r = len(array)-1


    for i in reversed(range(len(new))):
        vall= abs(array[l])
        valr = abs(array[r])

        if vall > valr:
            new[i] = vall*vall
            l+=1
        else:
            new[i] = valr*valr
            r-=1
    return new