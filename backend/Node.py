from typing import List

class Node:
    def __init__(self, level = None, parent = None, xCoordinate = None, yCoordinate = None, endNode = False, boldArrow = False):
        self.parent = parent
        self.level = level
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.children = []
        self.costs = ()
        self.endNode = endNode
        self.boldArrow = boldArrow

    def setX(self, xCoordinate):
        self.xCoordinate = int(xCoordinate)

    def setY(self, yCoordinate):
        self.yCoordinate = int(yCoordinate)

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
    

    def setChildren(self, children: list):
        self.children = children
    
    def getChildren(self):
        return self.children
    

    def setBoldArrow(self, boldArrow: bool):
        self.boldArrow = boldArrow

    def getBoldArrow(self):
        return self.boldArrow


    def addChild(self, child: 'Node'):
        if (self.children == None):
            self.children = []
        self.children.append(child)

    def removeChild(self, child: 'Node'):
        new_children = []
        for child_ in self.children:
            if child_ != child:
                new_children.append(child_)
        self.children = new_children


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
        best_cost = tempChildren[len(tempChildren) - 1].costs[label]
        return [child.costs for child in tempChildren if child.costs[label] == best_cost]
    

    # рекурсивная функция обхода графа, вызывающая некоторую
    # функцию для каждой вершины
    def graphTraverse(self, function):
        res = function(self)
        if res: return res
        for child in self.getChildren():
            res = child.graphTraverse(function)
            if res: return res

    # функция поиска ноды
    # в данном случае аргумент node - объект, с которым сравнивают
    # текущую ноду
    def findNode(self, click: List[int], nodeSize: int):
        delta = nodeSize // 2
        if(
            abs(self.getX() + delta - click[0]) <= delta and
            abs(self.getY() + delta - click[1]) <= delta
        ):
            return self
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
    
    def fillTreeMap(self, treeMap):
        try:
            treeMap[self.getLevel()].append(self)
        except KeyError:
            treeMap[self.getLevel()] = [self]
        for child in self.getChildren():
            child.fillTreeMap(treeMap)
    
    # рекурсивно ищет порядковый номер ноды на её уровне
    def findNodeLevelOrder(self, searchNode: 'Node'):
        # def fillTreeMap(node: 'Node', treeMap):
        #     try:
        #         treeMap[node.getLevel()].append(node)
        #     except KeyError:
        #         treeMap[node.getLevel()] = [node]
        #     for child in node.getChildren():
        #         fillTreeMap(child, treeMap)

        treeMap = {}
        # fillTreeMap(self, treeMap)
        self.fillTreeMap(treeMap)
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

    def updateTreeHeight(self, treeHeight):
        def recursiveMaxHeight(node):
            # если нет детей
            if not node.getChildren():
                return node.getLevel()

            maxHeight = 0
            for child in node.getChildren():
                maxHeight = max(maxHeight, recursiveMaxHeight(child))
            return maxHeight

        treeHeight = max(treeHeight, recursiveMaxHeight(self))
        return treeHeight
    
    def checkAllCosts(self):
        if not self.getCosts(): return False
        for child in self.children:
            child.checkAllCosts()
        return True
        
    def checkChildrenCosts(self):
        for child in self.children:
            if not child.getCosts():
                return False
        return True
    
    def findChildByCosts(self, costs):
        for child in self.children:
            if child.getCosts() == costs:
                return child
        return None
    
    # проверяет, что к данной ноде ведет стрелочка
    # если нода не корень и ее выигрыши совпадают с родительскими - возвращается
    # нода и родитель
    def checkArrow(self, root: 'Node'):
        if self.getLevel() > 1 and self.getCosts() == self.getParent().getCosts():
            treeMap = {}
            root.fillTreeMap(treeMap)
            # for i in range(treeMap[self.getLevel()].index(self)):
            #     if treeMap[self.getLevel()][i].getCosts() == self.getCosts():
            #         return None
            children = self.getParent().getChildren()
            for i in range(children.index(self)):
                if children[i].getCosts() == self.getCosts():
                    return None
            return (self, self.getParent())
        else:
            return None
        
    # все выигрыши от текущей ноды и выше должны совпадать
    def checkBoldArrow(self):
        node = self
        while node.getLevel() > 1:
            if node.getCosts() != node.getParent().getCosts():
                return False
            children = node.getParent().getChildren()
            for i in range(children.index(node)):
                if children[i].getCosts() == node.getCosts():
                    return None
            node = node.getParent()
        return True
    
    # исли на каждом уровне (кроме корня) ровно одна вершина с флагом - задача решена
    def checkTask(self):
        treeMap = {}
        self.fillTreeMap(treeMap)
        countEndNode = 0
        for level in treeMap:
            count = 0
            for node in treeMap[level]:
                # у всех нод, не являющихся листами, должна быть одна жирная стрелка на уровне,
                # а у листов - одна жирная стрелка на все листы
                if node.getBoldArrow():
                    if not node.getEndNode():
                        count += 1
                    else:
                        if node.checkBoldArrow():
                            countEndNode += 1
            # print(count)
            if level != 1 and count != 1 and not node.getEndNode():
                print('count: ' + str(count))
                return False
        if countEndNode != 1: 
            print('countEndNode: ' + str(countEndNode))
            return False
        else: return True