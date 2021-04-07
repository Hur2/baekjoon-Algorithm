#중위 후위 연산자 변형 알고리즘

num = int(input())
arr =[]
for i in range(num):
    arr.append(int(input()))

j=1
li=[]
result = []
error = 0
for i in arr:
    while j <= i:
        li.append(j)
        j+=1
        result.append("+")
    if li[-1] == i:
        li.pop()
        result.append("-")
    else:
        error = -1

if(error == -1):
    print("NO")
else:
    for i in result:
        print(i)
        


    




































