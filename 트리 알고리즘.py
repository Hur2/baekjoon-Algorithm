#트리 알고리즘

class tree:
    def __init__(self,a,b,c):
        self.data=a
        self.left=b
        self.right=c
def pre_order(node):
    print(node.data,end='')
    if node.left!='.':
        pre_order(trees[node.left])
    if node.right!='.':    
        pre_order(trees[node.right])
def in_order(node):
    if node.left!='.':
        in_order(trees[node.left])
    print(node.data,end='')
    if node.right!='.':    
        in_order(trees[node.right])
def post_order(node):
    if node.left!='.':
        post_order(trees[node.left])
    if node.right!='.':    
        post_order(trees[node.right])
    print(node.data,end='')
N=int(input())
trees={}
for i in range(N):
    a,b,c=input().split()
    trees[a]=tree(a,b,c)
pre_order(trees['A'])
print()
in_order(trees['A'])
print()
post_order(trees['A'])






























