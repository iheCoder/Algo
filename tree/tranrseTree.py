from typing import List

class Node:
    def __init__(self):
        pass
    def __init__(self,value,children):
        self.children=children
        self.value=value

def tranTree(nodes:List[Node],v,parentNode)->bool:
    res=False
    if nodes==None:
        return res
    for n in nodes:
        nc = Node(n.value, [])
        parentNode.children.append(nc)
        # 1. 遍历节点，如果匹配，则加入节点以及所有子节点到传入父节点下，并设置返回true
        if match(n.value,v):
            parentNode.children.remove(nc)
            res=True
            parentNode.children.append(n)

        # 2. 若不匹配，则当前节点加入父节点，并传入当前节点进行递归，
        else:
            cRes=tranTree(n.children,v,nc)
            # 3. 若递归返回为true，则设置返回为True；递归返回False，就在父节点移除当前节点
            if cRes==True:
                res=True
            else:
                parentNode.children.remove(nc)
    return res


def match(v1,v2):
    return v1==v2

if __name__ == '__main__':
    v=1
    node11=Node(2,None)
    node12=Node(2,None)
    n1c=[node11,node12]
    node1=Node(1,n1c)

    node21=Node(2,None)
    n2c=[node21]
    node2=Node(2,n2c)

    node31=Node(2,None)
    node321=Node(1,None)
    n32c=[node321]
    node32=Node(2,n32c)
    node3=Node(2,[node31,node32])

    nodes=[node1,node2,node3]

    pn=Node(None,[])
    r=tranTree(nodes,1,pn)
    print(r)


