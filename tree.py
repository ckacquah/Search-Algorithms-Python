# Author: Acquah Cyril Kofi
# Index N0: 10686868
# Date: 2/14/2021
# Copyright (C) 2021

import time
import math
import heapq
from tkinter import constants

LEFT = 0
RIGHT = 1

DEPTH_FIRST = 0
BREATH_FIRST = 1
UNIFORM_COST = 2


class Node:
    def __init__(self, key, x=0, y=0):
        self.path_cost = 0
        self.parent = None
        self.right = None
        self.left = None
        self.key = key
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def getPathCost(self):
        return self.path_cost

    def setPathCost(self, cost):
        self.path_cost = cost

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, point):
        self.x = point

    def setY(self, point):
        self.y = point

    def getKey(self):
        return self.key

    def hasLeft(self):
        return self.left != None

    def hasRight(self):
        return self.right != None

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent


class BinaryTree:
    def __init__(self):
        self.root = None
        self.found = None
        self.visited = None

    def getRoot(self):
        return self.root

    def insert(self, parentKey, node, direction):
        if self.root == None:
            self.root = node
        else:
            self.found = None
            self.searchPreOrder(self.root, parentKey)
        if self.found == None:
            return
        elif direction == LEFT:
            self.found.setLeft(node)
        elif direction == RIGHT:
            self.found.setRight(node)

        if node is not None:
            node.setParent(self.found)
            cost = abs(((self.found.getX() - node.getX()) ** 2) -
                       ((self.found.getY() - node.getY()) ** 2))
            cost = self.found.getPathCost() + math.sqrt(cost)
            node.setPathCost(cost)

    def search(self, searchKey, algorithm):
        start_time = int(round(time.time()*1000))
        start = self.root.getKey()
        end = searchKey
        self.visited = 0
        node = None
        name = None
        if algorithm == DEPTH_FIRST:
            node = self.depthFirstSearch(searchKey, visited=0)
            name = "Depth First"
        elif algorithm == BREATH_FIRST:
            node = self.breathFirstSearch(searchKey, visited=0)
            name = "Breath First"
        elif algorithm == UNIFORM_COST:
            node = self.uniformCostSearch(searchKey)
            name = "Uniform Cost"
        stop_time = int(round(time.time()*1000))
        return {
            "end": end,
            "node": node,
            "name": name,
            "start": start,
            "visited": self.visited,
            "time": str(stop_time - start_time) + "ms",
        }

    def _displayInOrder(self, node):
        if node == None:
            return
        if node.hasLeft():
            self._displayInOrder(node.getLeft())
        display(node.getKey())
        if node.hasRight():
            self._displayInOrder(node.getRight())

    def displayInOrder(self):
        return self._displayInOrder(self.root)

    def _displayPreOrder(self, node):
        if self.root == None:
            return
        display(node.getKey())
        if node.hasLeft():
            self._displayPreOrder(node.getLeft())
        if node.hasRight():
            self._displayPreOrder(node.getRight())

    def displayPreOrder(self):
        return self._displayPreOrder(self.root)

    def _displayPostOrder(self, node):
        if node == None:
            return
        if node.hasLeft():
            self._displayPostOrder(node.getLeft())
        if node.hasRight():
            self._displayPostOrder(node.getRight())
        display(node.getKey())

    def displayPostOrder(self):
        return self._displayPostOrder(self.root)

    def searchPreOrder(self, node, searchKey):
        if node == None:
            return
        if node.getKey() == searchKey:
            self.found = node
        self.searchPreOrder(node.getLeft(), searchKey)
        self.searchPreOrder(node.getRight(), searchKey)

    def uniformCostSearch(self, searchKey):
        node = self.root
        priority_queue = []
        visited = []
        heapq.heappush(priority_queue, (node.getPathCost(), id(node), node))
        while len(priority_queue) != 0:
            node = heapq.heappop(priority_queue)[2]
            if visited.count(node.getKey()) != 0:
                continue
            visited.append(node.getKey())
            if node.getKey() == searchKey:
                self.visited = len(visited)
                return node
            if node.hasLeft():
                heapq.heappush(priority_queue, (node.getLeft().getPathCost(), id(node.getLeft()), node.getLeft()))
            if node.hasRight():
                heapq.heappush(priority_queue, (node.getRight().getPathCost(), id(node.getLeft()), node.getRight()))

    def depthFirstSearch(self, searchKey, visited=0):
        lifo=[]
        lifo.append(self.root)
        self.visited=visited
        while len(lifo) != 0:
            current=lifo.pop()
            self.visited += 1
            if current.getKey() != searchKey:
                if current.hasLeft():
                    lifo.append(current.getLeft())
                if current.hasRight():
                    lifo.append(current.getRight())
            else:
                return current

    def breathFirstSearch(self, searchKey, visited=0):
        fifo=[]
        fifo.append(self.root)
        self.visited=visited
        while len(fifo) != 0:
            current=fifo.pop(0)
            self.visited += 1
            if current.getKey() != searchKey:
                if current.hasLeft():
                    fifo.append(current.getLeft())
                if current.hasRight():
                    fifo.append(current.getRight())
            else:
                return current


def display(key):
    print(key, end=" -> ")
