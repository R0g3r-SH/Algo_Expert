def Longest(array):
    longest = []
    maxpic= []
    #Search all pics
    for i in range(1,len(array)-1):
        prev=array[i-1]
        cur = array[i]
        next = array[i+1]
        if prev <= cur and cur > next:
            longest.append(i)

    for pic in range(len(longest)):
        curr = longest[pic]
        l = curr - 1
        r = curr+1
        steps = 0
        if (array[r] < array[curr] and array[curr] and array[l] < array[curr]):
            while array[l] < array[curr] and l >=0:
                l-=1
                steps+=1
                curr -=1
            curr = longest[pic]
            while r <= (len(array)-1) and array[r] < array[curr] :
                r+=1
                curr +=1
                steps+=1
            maxpic.append(steps)

    return max(maxpic)+1 if maxpic != [] else 0

array = [1, 2, 3, 3, 2, 1]
print(Longest(array))