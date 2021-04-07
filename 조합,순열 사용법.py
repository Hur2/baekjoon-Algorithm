#조합,수열 사용법

import itertools

num = list(map(int, input().split()))
li = [i for i in range(1, num[0]+1)]
nPr = list(itertools.permutations(li, num[1]))

for i in nPr:
    for j in i:
        print(j, end=" ")
    print("")



    




































