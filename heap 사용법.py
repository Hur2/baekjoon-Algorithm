#heap 사용법

import heapq
N=int(input())
arr=[]
heap=[]
for i in range(N):
    arr.append(int(input())) 
for i in arr:
    if i == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, i)


    




































