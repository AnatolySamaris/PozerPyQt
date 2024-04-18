from Node import Node
from TaskParser import TaskParser

parser = TaskParser(1)

n1 = Node(level = 1, xCoordinate=5, yCoordinate=5)
n2 = Node(parent = n1, level = 2, xCoordinate=100, yCoordinate=100)
n3 = Node(parent = n1, level = 2, xCoordinate=50, yCoordinate=50)
n4 = Node(parent=n2, level=3, xCoordinate=150, yCoordinate=150)
n1.addChild(n2)
n1.addChild(n3)
n2.addChild(n4)

#parser.createSchema(n1)
#parser.setCosts(parser.costs, parser.createEndNodesList(n1))

# n1.graphTraverse(
#     n1.graphTraverse(lambda: n1.recalculateNode(
#     n1, heightWindow=500, widthWindow=500, paintingZeroY=0, paintingZeroX=0, nodeSize=30, treeHeight=2
# ))
# )

#n1.graphTraverse(lambda node: node.recalculateNode(
#    n1, heightWindow=500, widthWindow=500, paintingZeroY=0, paintingZeroX=0, nodeSize=30, treeHeight=2
#))

#print(n1.getChildren()[1].getChildren()[1].getChildren()[0].getY())
#print(n1.getChildren()[1].getChildren()[1].getChildren()[0].getChildren()[1].getChildren()[1].getCosts())


res = n1.graphTraverse(
    lambda node: node.findNode(
        [150, 150], 40
    )
)

height = 1
height = n1.updateTreeHeight(height)
print(height)

# print(res.getLevel())