# sendo:
# A -> C -> F
# \> B -> D
#     \> E



def BinaryTree(r):
    return [r,[],[]]

def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.inset(1,[new_branch,t,[]])
    else:
        root.insert(1,[new_branch,[],[]])
    
    return root

def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.inset(1,[new_branch,t,[]])
    else:
        root.insert(1,[new_branch,[],[]])
    
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root,new_val):
    root[0] = new_val

def get_left_child(r):
    return root

# def 

r = BinaryTree(2)
print(r)
print(get_root_val(r))