class Node:
    def __init__(self, level = None, parent = None, xCoordinate = None, yCoordinate = None):
        self.parent = parent
        self.level = level
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.children = None
        self.costs = None
        self.endNode = False

        # STATIC FIELDS
        window_width = 0
        window_height = 0
        node_size = 0
        x_paint_zero = 0
        y_paint_zero = 0
        tree_height = 0

    def setup_static(window_width, window_height, x_painting_zero, y_painting_zero, node_size, tree_height=0):
        Node.window_width = window_width
        Node.window_height = window_height
        Node.x_painting_zero = x_painting_zero
        Node.y_painting_zero = y_painting_zero
        Node.node_size = node_size
        Node.tree_height = tree_height


    def setX(self, xCoordinate):
        self.xCoordinate = xCoordinate

    def setY(self, yCoordinate):
        self.yCoordinate = yCoordinate

    def getX(self):
        return self.xCoordinate

    def getY(self):
        return self.yCoordinate
    

    def setLevel(self, level):
        self.level = level

    def getLevel(self):
        return self.level    
    

    def setParent(self, parent: 'Node'):
        self.parent = parent

    def getParent(self):
        return self.parent


    def setCosts(self, costs):
        self.costs = costs

    def getCosts(self):
        return self.costs
    

    def setEndNode(self, endNode: bool):
        self.endNode = endNode

    def getEndNode(self):
        return self.endNode
    

    def setPosition(self, xCoordinate, yCoordinate):
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate

    def getPosition(self):
        return [self.xCoordinate, self.yCoordinate]
    

    def getChildren(self):
        return self.children


    def addChild(self, child: 'Node'):
        if (self.children == None):
            self.children = []
        self.children.append(child)

    def deleteChildren(self):
        self.children.clear()

    def countChildren(self):
        return len(self.children)
    

    def findBestCosts(self):
        label = (self.level + 1) % 2; # 0 -> A, 1 -> B
        tempChildren = self.children
        tempChildren.sort(
            key=lambda x: x.costs[label]
        )
        return tempChildren[len(tempChildren) - 1].costs
    

    # рекурсивная функция обхода графа, вызывающая некоторую
    # функцию для каждой вершины
    def graphTraverse(self, function):
        function()
        for child in self.getChildren():
            child.graphTraverse(function)

    # функция поиска ноды
    # в данном случае аргумент node - объект, с которым сравнивают
    # текущую ноду
    def findNode(self, node: 'Node', nodeSize: int):
        if(
            abs(self.getX() - node.getX()) <= nodeSize and
            abs(self.getY() - node.getY()) <= nodeSize
        ):
            return node
        else:
            return None

    # рекурсивно считает число нод на уровне
    # вызывается как метод вершины root,
    # при этом searchNode - нода, для которой нужно определить
    # число нод на уровне
    def countLevelNodes(self, searchNode: 'Node'):
        if self.getLevel() == searchNode.getLevel():
            return 1
        else:
            count = 0
            for child in self.getChildren():
                count += child.countLevelNodes(searchNode)
            return count
    
    # рекурсивно ищет порядковый номер ноды на её уровне
    def findNodeLevelOrder(self, searchNode: 'Node'):
        def fillTreeMap(node: 'Node', treeMap):
            try:
                treeMap[node.getLevel()].append(node)
            except KeyError:
                treeMap[node.getLevel()] = node
            for child in node.getChildren():
                fillTreeMap(child, treeMap)

        treeMap = {}
        fillTreeMap(self, treeMap)
        return treeMap[searchNode.getLevel()].index(searchNode) + 1

    def recalculateNode(self, root: 'Node', heightWindow, widthWindow, paintingZeroY, paintingZeroX, nodeSize, treeHeight):
        # считаем Y коодинату
        spaceVertical = (heightWindow - paintingZeroY - nodeSize * treeHeight) / (treeHeight + 1)
        self.setY(paintingZeroY + nodeSize * (self.getLevel() - 1) + spaceVertical * (self.getLevel() - 1))

        # считаем X координату
        levelNodesAmount = root.countLevelNodes(self)
        nodeLevelOrder = root.findNodeLevelOrder(self)
        spaceHoriz = (widthWindow - nodeSize * levelNodesAmount) / (levelNodesAmount + 1)
        self.setX(paintingZeroX + nodeSize * (nodeLevelOrder - 1) + spaceHoriz * nodeLevelOrder)

    def updateTreeHeight(treeHeight, root: 'Node'):
        def recursiveMaxHeight(self):
            # если нет детей
            if not self.getChildren():
                return self.getLevel()

            maxHeight = 0
            for child in self.getChildren():
                maxHeight = max(maxHeight, recursiveMaxHeight(child))
            return maxHeight

        treeHeight = max(treeHeight, recursiveMaxHeight(root))
