#dfs

from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(li):
    maxi=1
    queue = deque(li)
    while queue:
        v = queue.popleft()
        for i in range(4):
            x_=v[0]+dx[i]
            y_=v[1]+dy[i]
            if 0<=x_<N and 0<=y_<M and tmt[x_][y_]==0:
                queue.append([x_, y_])
                tmt[x_][y_]=tmt[v[0]][v[1]]+1
                if tmt[x_][y_]>maxi:
                    maxi=tmt[x_][y_]
    for i in tmt:
        for j in i:
            if j==0:
                return 0
    return maxi    

M,N=map(int,input().split())
tmt=[]
li=[]
for i in range(N):
    tmt.append(list(map(int,input().split())))
for i in range(N):
    for j in range(M):
        if tmt[i][j]==1:
            li.append([i, j])
print(bfs(li)-1)



    




































