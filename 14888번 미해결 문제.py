#14888번 미해결 문제

def recur(s, e):
    if(s == e):
        total = A[0]
        for i in range(len(oper)):
            total += oper[i] + A[i+1]
            total = str(eval(total))
        li.append(total)
        return
    
    for i in range(s, e):
        if oper[s] == oper[i] and s != i:
            continue
        else:
            oper[s], oper[i] = oper[i], oper[s]
            recur(s+1, e)
            oper[s], oper[i] = oper[i], oper[s]
import time

s = time.time()

A = input().split()
li = list(map(int, input().split()))
ex = ['+', '-', '*', '//']
oper = []

print(divmod(-3, 2)[0])

for i in range(4):
    for j in range(li[i]):
        oper.append(ex[i])
li=[]
recur(0, len(oper))
li.sort()
print(max(li), min(li))
e = time.time()
print(e-s)
"""

"""
N=int(input())
M=int(input())
arr=[]
graph=[[] for i in range(N+1)]
visited=[False]*(N+1)
A=0
for i in range(M):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)



    




































