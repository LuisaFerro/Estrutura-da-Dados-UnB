from estudo_arvore_POO import *

def bt_show_withtab(node,level):
    for i in range(level):
        print('\t',end='')
    if node:
        print(f'{node.data}')
    else:
        print('X\n')

def bt_show(root,level):
    if not root:
        bt_show_withtab(None, level)
        return
    
    bt_show(root.right,level+1)
    bt_show(root,level)
    bt_show(root.left,level+1)

def bt_left_rotation(root): 
    if root and root.right:
        aux = root
        root = root.right
        aux.right = root.left
        root.left = aux
    return root


def bt_right_rotation(root): 
    if root and root.left:
        aux = root
        root = root.left
        aux.left = root.right
        root.right = aux
    return root

def bst_dsw_backbone(root):
    if root:
        while root and root.left:
            root = bt_right_rotation(root)
        
        root.right = bst_dsw_backbone(root.right)
    
    return root
            
def bst_dsw_compress(root,rotation_number):
    root = bst_dsw_backbone(root)
    backbone_size = root.altura()-1
    rotation_number = backbone_size//2
    
    while rotation_number > 0:
        bst_dsw_compress(root,rotation_number)
        backbone_size -= rotation_number + 1
        rotation_number = backbone_size//2

root = ArvoreBinariaBusca(10)
root = insere(root,ArvoreBinariaBusca(7))
root = insere(root,ArvoreBinariaBusca(8))
root = insere(root,ArvoreBinariaBusca(9))

print('arvore balanceada')
