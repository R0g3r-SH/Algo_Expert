
#Time O(Klogn)
# def topKFrequent(nums, k):
#         setnums = {}
#         for i in nums:
#             if i in setnums:
#                 setnums[i]+=1
                
#             else:
#                 setnums[i] = 1
#         sort_orders = sorted(setnums.items(), key=lambda x: x[1], reverse=True)
#         out = []
#         for i in sort_orders:
#             if k>0:
#                 out.append(i[0])
#             else:
#                 break
#             k-=1
#         return out
        
# Clever Response in Time O(n) Linear Time




def topKFrequent(nums, k):
    count ={}

# 2022-06-16-03-06-25.png

nums = [3,0,1,0]
k = 1
print(topKFrequent(nums, k))