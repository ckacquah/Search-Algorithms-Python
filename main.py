# Author: Acquah Cyril Kofi
# Index N0: 10686868
# Date: 2/14/2021
# Copyright (C) 2021

from tkinter import messagebox
from tree import *
from app import *

app = Application()
tree = BinaryTree()


def traceRoute(node):
    route = []
    while node is not None:
        route.append(node)
        node = node.getParent()
    return route


def drawRoute(route):
    if len(route) == 0:
        return
    node = route.pop()
    while len(route) != 0:
        nextNode = route[-1]
        app.getGraph().route((node.getX(), node.getY()),
                             (nextNode.getX(), nextNode.getY()))
        node = route.pop()


def plotTowns(node):
    if node is None:
        return
    plotTowns(node.getLeft())
    plotTowns(node.getRight())
    app.getGraph().plot(node.getX(), node.getY(), node.getKey())


def connectNodes(node):
    if node is None:
        return
    child = node.getLeft()
    if child is not None:
        app.getGraph().connect((node.getX(), node.getY()), (child.getX(), child.getY()))
    child = node.getRight()
    if child is not None:
        app.getGraph().connect((node.getX(), node.getY()), (child.getX(), child.getY()))
    connectNodes(node.getLeft())
    connectNodes(node.getRight())


def command(Event):
    destination = app.getDestination()
    structure = tree.search(destination, app.getAlgorithm())
    node = structure["node"]

    if node is not None:
        app.getGraph().clear()
        route = traceRoute(node)
        drawRoute(route)
        plotTowns(tree.getRoot())
        connectNodes(tree.getRoot())
        app.getGraph().getCanvas().grid(row=1, columnspan=6)
        app.updateFooter(structure)
        app.getGraph().draw()
    else:
        messagebox.showerror("Invalid Input", "Town you entered was not found!")


if __name__ == "__main__":

    # create and define the structure of the binary tree
    x = Node("Accra", x=0, y=200)
    tree.insert(None, x, LEFT)

    x = Node("Tema", x=40, y=120)
    tree.insert("Accra", x, LEFT)

    x = Node("Achimota", x=80, y=180)
    tree.insert("Accra", x, RIGHT)

    x = Node("Dansoman", x=80, y=120)
    tree.insert("Achimota", x, LEFT)

    x = Node("Kaneshie", x=60, y=80)
    tree.insert("Dansoman", x, LEFT)

    x = Node("Mamprobi", x=100, y=80)
    tree.insert("Dansoman", x, RIGHT)

    x = Node("Kasoa", x=100, y=160)
    tree.insert("Achimota", x, RIGHT)

    x = Node("Mankessim", x=140, y=180)
    tree.insert("Kasoa", x, RIGHT)

    x = Node("Boduase", x=140, y=140)
    tree.insert("Kasoa", x, LEFT)

    tree.displayPreOrder()
    print()

    plotTowns(tree.getRoot())
    connectNodes(tree.getRoot())

    app.onClick(command)

    app.getGraph().draw()
    app.run()
