#dp를 통해서 최소거리 찾기
"""
N=int(input())
house=[]
d=[[0]*3 for i in range(N)]
for i in range(N):
    house.append(list(map(int,input().split())))

for i in range(1, N):
    for j in range(3):
        mi = 1e9
        for k in range(3):
            if j == k:
                continue
            mi = min(house[i][j]+house[i-1][k], mi)
        house[i][j] = mi
print(min(house[N-1][0], house[N-1][1], house[N-1][2]))
"""
