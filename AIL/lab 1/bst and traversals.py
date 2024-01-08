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
