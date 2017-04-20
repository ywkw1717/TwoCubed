#!/usr/bin/env python
# coding: utf-8

#################################
#      Cube State               #
#                               #
#       -------                 #
#       |U1|U2|                 #
#       |U3|U4|                 #
# ------|-----|------------     #
# |L1|L2|F1|F2|R1|R2|B1|B2|     #
# |L3|L4|F3|F4|R3|R4|B3|B4|     #
# ------|-----|------------     #
#       |D1|D2|                 #
#       |D3|D4|                 #
#       -------                 #
#################################

from cube import *
from node import *
import copy

# procedure (stack)
pastProcedure= []

def solve(_cube):
  root = Node()
  # node1 = Node()
  # rootNode.setChild(node1)
  # node1.setNext(node2)
  append('root', None, root)
  node1 = Node()
  node2 = Node()
  node3 = Node()
  node4 = Node()
  node5 = Node()

  append('node1', root, node1)
  append('node1-1', node1, node2)
  append('node1-2', node1, node3)
  append('node2', root, node4)
  append('node2-1', node2, node5)

  show_tree_dfs(root)


  cube1 = copy.deepcopy(_cube)
  cube1.rRotation()
  pastProcedure.append('R')

  print cube1.getLayout()
  print pastProcedure

  cube1.rprimeRotation()
  pastProcedure.pop(0)

  print cube1.getLayout()
  print pastProcedure
#
#     cube2 = copy.deepcopy(_cube)
#     cube2.rprimeRotation()
#
#     cube3 = copy.deepcopy(_cube)
#     cube3.r2Rotation()
#
#     cube4 = copy.deepcopy(_cube)
#     cube4.uRotation()
#
#     cube5 = copy.deepcopy(_cube)
#     cube5.uprimeRotation()
#
#     cube6 = copy.deepcopy(_cube)
#     cube6.u2Rotation()
#
#     cube7 = copy.deepcopy(_cube)
#     cube7.fRotation()
#
#     cube8 = copy.deepcopy(_cube)
#     cube8.fprimeRotation()
#
#     cube9 = copy.deepcopy(_cube)
#     cube9.f2Rotation()
#
#     for i in range(1, 9):
#         for j in range(1, 9):
#             for k in range(1, 9):
#                 for l in range(1, 9):
#                     for m in range(1, 9):
#                         for n in range(1, 9):
#                             for o in range(1, 9):
#                                 for p in range(1, 9):
#                                     for q in range(1, 9):
#
#     print cube1.getLayout()
#     print cube2.getLayout()


def main():
    print 'This is the Rubik\'s Cube(2x2x2) solver'
    print """
#################################
#      Cube State               #
#                               #
#       -------                 #
#       |U1|U2|                 #
#       |U3|U4|                 #
# ------|-----|------------     #
# |L1|L2|F1|F2|R1|R2|B1|B2|     #
# |L3|L4|F3|F4|R3|R4|B3|B4|     #
# ------|-----|------------     #
#       |D1|D2|                 #
#       |D3|D4|                 #
#       -------                 #
#################################
    """

    # print 'Input the first state >>',
    #
    # cube = Cube('BUFFDDLLRRDFURDFBRLUBLBU')
    # layout = raw_input()
    cube = Cube('UUUULLLLFFFFRRRRBBBBDDDD')
    # cube = Cube(layout)

    # rotation Test
    # count = 1
    # while(True):
    #     print ''.join(cube.getLayout())
    #     cube.rRotation()
    #     cube.lRotation()
    #     cube.uprimeRotation()
    #
    #     if (''.join(cube.getLayout()) == 'UUUULLLLFFFFRRRRBBBBDDDD'):
    #         break
    #     else:
    #         count = count + 1
    #
    # print '\n' + ''.join(cube.getLayout())
    # print '\n' + 'total: ' + str(count)
    # print '\n' + 'procedure: ' + cube.getProcedure()

    solve(cube)

if __name__ == '__main__':
    main()
