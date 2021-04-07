#벨만포드 알고리즘

import sys
INF=int(10001)
input = sys.stdin.readline
def bf(start):
    dist[start]=0
    for i in range(V):
        for j in graph:
            if dist[j[1]]>dist[j[0]]+j[2]:
                dist[j[1]]=dist[j[0]]+j[2]
                if i==V-1:
                    return True
    return False
T=int(input())
for i in range(T):
    V,E,W=map(int,input().split())
    graph=[]
    temp=[]
    dist=[INF]*(V+1)
    for j in range(E):
        a,b,c = map(int,input().split())
        graph.append((a,b,c))
        graph.append((b,a,c))
    for j in range(W):
        a,b,c = map(int,input().split())
        graph.append((a,b,-c))
    if bf(1):
        print("YES")
    else:
        print("NO")





    




































