from typing import List, Tuple

class Node:
    """
    Класс вершины.
    Параметры вершины задаются в методе __init__.
    """
    def __init__(self, level = None, parent = None, xCoordinate = None, yCoordinate = None, endNode = False, boldArrow = False):
        self.parent = parent
        self.level = level
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.children = []
        self.costs = ()
        self.endNode = endNode
        self.boldArrow = boldArrow

    def setX(self, xCoordinate: int) -> None:
        self.xCoordinate = int(xCoordinate)

    def setY(self, yCoordinate: int) -> None:
        self.yCoordinate = int(yCoordinate)

    def getX(self) -> int:
        return self.xCoordinate

    def getY(self) -> int:
        return self.yCoordinate
    

    def setLevel(self, level: int) -> None:
        self.level = level

    def getLevel(self) -> int:
        return self.level    
    

    def setParent(self, parent: 'Node') -> None:
        self.parent = parent

    def getParent(self) -> 'Node':
        return self.parent


    def setCosts(self, costs: Tuple[int]) -> None:
        self.costs = costs

    def getCosts(self) -> Tuple[int]:
        return self.costs
    

    def setEndNode(self, endNode: bool):
        self.endNode = endNode

    def getEndNode(self) -> bool:
        return self.endNode
    

    def setPosition(self, xCoordinate: int, yCoordinate: int) -> None:
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate

    def getPosition(self) -> List[int]:
        return [self.xCoordinate, self.yCoordinate]
    

    def setChildren(self, children: list) -> None:
        self.children = children
    
    def getChildren(self) -> List['Node']:
        return self.children
    

    def setBoldArrow(self, boldArrow: bool) -> None:
        self.boldArrow = boldArrow

    def getBoldArrow(self) -> bool:
        return self.boldArrow


    def addChild(self, child: 'Node') -> None:
        """
        Добавляет потомка в список потомков вершины, от которой вызывается метод.
        """
        if (self.children == None):
            self.children = []
        self.children.append(child)

    def removeChild(self, child: 'Node') -> None:
        """
        Удаляет указанного потомка из списка потомков вершины, от которой вызывается метод.
        """
        new_children = []
        for child_ in self.children:
            if child_ != child:
                new_children.append(child_)
        self.children = new_children


    def deleteChildren(self) -> None:
        """
        Удаляет всех потомков вершины.
        """
        self.children.clear()

    def countChildren(self) -> int:
        """
        Возвращает число потомков вершины.
        """
        return len(self.children)

    def findBestCosts(self) -> Tuple[int]:
        """
        Возвращает наиболее выгодную из имеющихся пару выигрышей для вершины, 
        от которой вызывается метод.
        """
        label = (self.level + 1) % 2; # 0 -> A, 1 -> B
        tempChildren = self.children.copy()
        tempChildren.sort(
            key=lambda x: x.costs[label]
        )
        best_cost = tempChildren[len(tempChildren) - 1].costs[label]
        return [child.costs for child in tempChildren if child.costs[label] == best_cost]
    

    def graphTraverse(self, function):
        """
        Рекурсивно обходит граф и вызывает некоторую функцию, переданную 
        в качестве аргумента, для каждой вершины.
        """
        res = function(self)
        if res: return res
        for child in self.getChildren():
            res = child.graphTraverse(function)
            if res: return res

    def findNode(self, click: List[int], nodeSize: int):
        """
        Определяет, попадают ли координаты клика в область вершины.
        В качестве аргументов принимает координаты клика и размер вершины.
        """
        delta = nodeSize // 2
        if(
            abs(self.getX() + delta - click[0]) <= delta and
            abs(self.getY() + delta - click[1]) <= delta
        ):
            return self
        else:
            return None

    def countLevelNodes(self, searchNode: 'Node') -> int:
        """
        Рекурсивно считает число нод на уровне.
        Должен вызываться как метод вершины root.
        При этом аргумент searchNode - вершина, для которой нужно определить число нод на уровне.
        """
        if self.getLevel() == searchNode.getLevel():
            return 1
        else:
            count = 0
            for child in self.getChildren():
                count += child.countLevelNodes(searchNode)
            return count
    
    def fillTreeMap(self, treeMap):
        """
        Заполняет переданный в качестве аргумента словарь следующим образом: 
        в качестве ключей выступают номера уровней, в качестве значений - списки вершин на этих уровнях.
        """
        try:
            treeMap[self.getLevel()].append(self)
        except KeyError:
            treeMap[self.getLevel()] = [self]
        for child in self.getChildren():
            child.fillTreeMap(treeMap)
    
    def findNodeLevelOrder(self, searchNode: 'Node') -> int:
        """
        Рекурсивно ищет порядковый номер вершины на ее уровне.
        """
        treeMap = {}
        self.fillTreeMap(treeMap)
        return treeMap[searchNode.getLevel()].index(searchNode) + 1

    def recalculateNode(self, root: 'Node', heightWindow, widthWindow, paintingZeroY, paintingZeroX, nodeSize, treeHeight):
        """
        Вычисляет координаты вершины, от которой вызывается метод.
        Используется при изменении схемы каким-либо образом: добавлении/удалении вершины.
        В качестве арргументов принимает необходимые для вычислений параметры окна.
        """
        # считаем Y коодинату
        spaceVertical = (heightWindow - paintingZeroY - nodeSize * treeHeight) / (treeHeight + 1)
        self.setY(paintingZeroY + nodeSize * (self.getLevel() - 1) + spaceVertical * (self.getLevel() - 1))

        # считаем X координату
        levelNodesAmount = root.countLevelNodes(self)
        nodeLevelOrder = root.findNodeLevelOrder(self)
        spaceHoriz = (widthWindow - nodeSize * levelNodesAmount) / (levelNodesAmount + 1)
        self.setX(paintingZeroX + nodeSize * (nodeLevelOrder - 1) + spaceHoriz * nodeLevelOrder)

    def updateTreeHeight(self, treeHeight: int) -> int:
        """
        Обновляет высоту дерева, которая передается в качестве аргумента.
        Вызывается от корневой вершины при изменении числа уровней.
        """
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
    
    def checkAllCosts(self) -> bool:
        """
        Рекурсивно проверяет, всем ли вершинам заданы выигрыши.
        """
        if not self.getCosts(): return False
        for child in self.children:
            child.checkAllCosts()
        return True
        
    def checkChildrenCosts(self) -> bool:
        """
        Проверяет, всем ли потомкам вершины заданы выигрыши.
        """
        for child in self.children:
            if not child.getCosts():
                return False
        return True
    
    def findChildByCosts(self, costs):
        """
        Определяет, есть ли среди потомков вершины потомок с заданными выигрышами
        (выигрыши передаются в качестве аргументов).
        """
        for child in self.children:
            if child.getCosts() == costs:
                return child
        return None
        
    def checkArrow(self, root: 'Node'):
        """
        Проверяет, ведет ли к данной вершине стрелка.
        Если да - возвращает данную вершину и ее родителя.
        """
        if self.getLevel() > 1 and self.getCosts() == self.getParent().getCosts():
            treeMap = {}
            root.fillTreeMap(treeMap)
            children = self.getParent().getChildren()
            for i in range(children.index(self)):
                if children[i].getCosts() == self.getCosts():
                    return None
            return (self, self.getParent())
        else:
            return None