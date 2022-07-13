#Time O(n) whwre n is the length of the larguesr list
#Space O(I) were i is the number of intersections betwen the two lists
def intervalIntersection(A, B):
    out = [] 
    #using 2 pointers
    Aptr ,Bptr = 0,0
    #handle the length of te vectors
    #know were is an intersection
    while(Aptr<len(A) and Bptr<len(B)):
        if (B[Bptr][0]<=A[Aptr][1] and A[Aptr][0] <= B[Bptr][1]):
            #the formula es max(first values ) min(second Values)
            out.append([max(A[Aptr][0],B[Bptr][0]),min(A[Aptr][1],B[Bptr][1])])
        # no intersection
        if(A[Aptr][1]>B[Bptr][1]):
            Bptr+=1
        else:
            Aptr+=1

    return out


firstList, secondList = [[0, 2], [5, 10], [13, 23]],[]
print(intervalIntersection(firstList, secondList))
