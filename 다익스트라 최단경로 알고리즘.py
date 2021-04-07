#다익스트라, 최단거리

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue      
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))
import sys
import heapq
INF=int(1e9)
input = sys.stdin.readline

V,E=map(int,input().split())
start=int(input())
graph=[[] for i in range(V+1)]
distance=[INF]*(V+1)

for i in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
dijkstra(start)

for i in range(1, V+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])



    




































