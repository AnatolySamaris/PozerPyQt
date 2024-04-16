from Node import Node

n1 = Node(level = 1)
n2 = Node(parent = n1, level = 2)
n3 = Node(parent = n1, level = 2)
n1.addChild(n2)
n1.addChild(n3)

# n1.graphTraverse(
#     n1.graphTraverse(lambda: n1.recalculateNode(
#     n1, heightWindow=500, widthWindow=500, paintingZeroY=0, paintingZeroX=0, nodeSize=30, treeHeight=2
# ))
# )

n1.graphTraverse(lambda node: node.recalculateNode(
    n1, heightWindow=500, widthWindow=500, paintingZeroY=0, paintingZeroX=0, nodeSize=30, treeHeight=2
))

print(n1.getY())
print(n2.getY())