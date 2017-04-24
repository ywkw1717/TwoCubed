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
import list_generator as gen
import copy

# procedure (stack)
pastProcedure= []

def solve(_cube, depth):
  cube = _cube
  print cube.getLayout()
  # cube1 = copy.deepcopy(_cube)

  # print cube.getLayout()
  # print pastProcedure
  #
  # cube.rprimeRotation()
  # pastProcedure.pop(0)
  #
  # print cube.getLayout()
  # print pastProcedure

  gen.recursive(gen.proc, gen.WORD_NUM)

  for i in gen.procedure:
      print i
      cube.rotation('R\'')
      # cube.rotation(i)
      print cube.getLayout()

def dfs(_cube, _depth):
    cube = _cube
    depth = _depth + 1

    if (''.join(cube.getLayout()) == 'UUUULLLLFFFFRRRRBBBBDDDD'):
        return True
    elif (depth == 11):
        pastProcedure.pop(0)
        return cube.rprimeRotation()
    else:
        cube.rRotation()
        pastProcedure.append('R')

        dfs(cube)


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

    solve(cube, 11)

if __name__ == '__main__':
    main()
