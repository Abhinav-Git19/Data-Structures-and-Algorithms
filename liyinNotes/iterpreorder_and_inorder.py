
class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

root =TreeNode(0)
stack = []
cur = root

preorder = [] #This order is obtained whene elements is pushed into stack
inorder = [] #This order is obtained when elements is poped from stack
while stack or cur:
    while cur:
        preorder.append(cur.data)
        stack.append(cur)
        cur = cur.left
    
    cur = stack.pop()
    inorder.append(cur.data)
    cur=cur.right


