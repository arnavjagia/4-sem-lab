class Node:  
    def __init__(self, val):  
        self.val, self.lchild, self.rchild= val, None, None
        
def insert(root, x):  
    if root is None:  
        return Node(x)  
    else:  
        if root.val == x:  
            return root  
        elif root.val < x:  
            root.rchild = insert(root.rchild, x)  
        else:  
            root.lchild = insert(root.lchild, x)  
    return root  
    
def inorderTraversal(root):  
    if root:  
        inorderTraversal(root.lchild)  
        print(root.val, end = " ")  
        inorderTraversal(root.rchild)

def preorderTraversal(root):  
    if root:  
        print(root.val, end = " ")  
        preorderTraversal(root.lchild)  
        preorderTraversal(root.rchild)

def postorderTraversal(root):  
    if root:  
        postorderTraversal(root.lchild)  
        postorderTraversal(root.rchild)
        print(root.val, end = " ")  
        
root = Node(25)
for val in [4,10,12,15,18,22,24,31,35,44,50,66,70,90]:
    insert(root, val)
inorderTraversal(root)
print("\n")
preorderTraversal(root)
print("\n")
postorderTraversal(root)
print("\n")

"""
4 10 12 15 18 22 24 25 31 35 44 50 66 70 90 

25 4 10 12 15 18 22 24 31 35 44 50 66 70 90 

24 22 18 15 12 10 4 90 70 66 50 44 35 31 25 
"""
