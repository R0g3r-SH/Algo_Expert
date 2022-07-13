
import heapq
def kClosest(points,k):
    #create a heap
    heap =[]
    for x,y in points:
        #using part of the formula of distance
        dis = (x**2)+(y**2)
        heap.append([dis,x,y])
    heapq.heapify(heap)
    res=[]
    while k>0:
        dis,x,y = heapq.heappop(heap)
        res.append([x,y])                       
        k-=1
    print(res)
    return res

points =[[3,3],[5,-1],[-2,4]]
k = 2

print(kClosest(points,k))