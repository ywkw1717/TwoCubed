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
import sys
import re
from tqdm import tqdm

# Procedure list
pastProcedure= []

# The pattern that half of the bottoms finish
pattern = re.compile('......LL..FF..RR..BBDDDD|UUUULL..FF..RR..BB......|U.U.LLLLF.F......B.BD.D.|U.U..L.LFFFFR.R.....DD..|.U.U.....F.FRRRRB.B..D.D|UU..L.L......R.RBBBB..DD')

def solve(_cube, depth):
    cube = _cube
    print cube.getLayout()

    print 'list generating...'
    procedure = gen.generator(gen.proc, gen.WORD_NUM)
    print '-------------------------'
    count = 1

    for i in procedure:
        cube1= copy.deepcopy(cube)
        procedure_split = i.split(' ')
        pastProcedure.append(i)

        sys.stdout.write('\rnum of rotation: %d' % count)
        sys.stdout.flush()

        for j in procedure_split:
            cube1.rotation(j)

            if pattern.findall(''.join(cube1.getLayout())):
                print "\n\n\nhalf FOUND!!!\n\n\n"
                print ''.join(pastProcedure)
                return

                for k in procedure:
                    cube2 = copy.deepcopy(cube1)
                    procedure_split = i.split(' ')
                    pastProcedure.append(k)

                    print count

                    for l in procedure_split:
                        cube1.rotation(l)

                        if (''.join(cube2.getLayout()) == 'UUUULLLLFFFFRRRRBBBBDDDD'):

                            print "FOUND!!!"
                            print ''.join(pastProcedure)

                            return
                        # else:
                        #     cube2.rotation(l)

                    pastProcedure.remove(k)
                    count = count + 1
            # else:
            #     cube1.rotation(j)

        pastProcedure.remove(i)
        count = count + 1

    print "Not Found..."


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
    cube = Cube('FFFRLLBUDUBDFDRBRULLRBUD')
    # cube = Cube('DUDURRLLFBFBLLRRFBFBDUDU')
    # layout = raw_input()
    # cube = Cube(layout)
    # cube = Cube('UUUULRLLBFFFRLRRFBBBDDDD')

    solve(cube, 11)

if __name__ == '__main__':
    main()
