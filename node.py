#!/usr/bin/env python
import copy


class Node:
    def __init__(self):
        self.name = None
        self.child = None
        self._next = None
        self.depth = None

    def getName(self):
        return self.name

    def getChild(self):
        return self.child

    def getNext(self):
        return self._next

    def getDepth(self):
        return self.depth

    def setName(self, name):
        self.name = name

    def setChild(self, child):
        self.child = child

    def setNext(self, _next):
        self._next = _next

    def setDepth(self, depth):
        self.depth = depth


def append(name, parent, node):
    node.setName(name)
    node.setDepth(0)
    node.setChild(None)
    node.setNext(None)

    if (parent is None):
        return

    node.setDepth(parent.getDepth() + 1)

    if (parent.getChild() is None):
        parent.setChild(node)
    else:
        last = copy.deepcopy(parent.getChild())
        while (last.getNext() is not None):
            last = copy.deepcopy(last.getNext())
        last.setNext(node)


def display(node):
    for i in range(0, node.getDepth()):
        print ' '
    print '- %s\n' % node.getName()


def show_tree_dfs(node):
    if (node is None):
        return
    display(node)
    if (node.getChild()): show_tree_dfs(node.getChild())
    if (node.getChild()): show_tree_dfs(node.getNext())

