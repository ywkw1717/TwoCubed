#!/usr/bin/env python


import ConfigParser
from color import U1, U2, U3, U4, L1, L2, L3, L4, F1, F2, F3, F4, R1, R2, R3, R4, B1, B2, B3, B4, D1, D2, D3, D4

inifile = ConfigParser.SafeConfigParser()
inifile.read('./config.ini')


class Cube:
    """ The Cube Class"""
    """ solved cube layout is UUUULLLLFFFFRRRRBBBBDDDD """

    # constructor
    def __init__(self, layout):
        self.layout = list(layout)  # change a layout from strings into list
        self.colors = [
            inifile.get('settings', 'U'),
            inifile.get('settings', 'L'),
            inifile.get('settings', 'F'),
            inifile.get('settings', 'R'),
            inifile.get('settings', 'B'),
            inifile.get('settings', 'D')
        ]
        self.procedure = ''

    def getLayout(self):
        return self.layout

    def getColor(self, num):
        return self.colors[num]

    def getProcedure(self):
        return self.procedure

    def setProcedure(self, proc):
        self.procedure = self.procedure + proc

    # 90 degrees right on R side
    def rRotation(self):
        self.swapColor(F2, U2)  # F2 - U2
        self.swapColor(F4, U4)  # F4 - U4
        self.swapColor(F2, D2)  # F2 - D2
        self.swapColor(F4, D4)  # F4 - D4
        self.swapColor(D2, B3)  # D2 - B3
        self.swapColor(D4, B1)  # D4 - B1

        self.rightRotation('R')

        self.setProcedure('R')

    # 90 degrees left on R side
    def rprimeRotation(self):
        self.swapColor(B1, U4)  # B1 - U4
        self.swapColor(B3, U2)  # B3 - U2
        self.swapColor(B1, F4)  # B1 - F4
        self.swapColor(B3, F2)  # B3 - F2
        self.swapColor(B1, D4)  # B1 - D4
        self.swapColor(B3, D2)  # B3 - D2

        self.leftRotation('R')

        self.setProcedure('R\'')

    # 180 degrees right on R side
    def r2Rotation(self):
        self.rRotation()
        self.rRotation()
        self.setProcedure('R2')

    # 90 degrees right on L side
    def lRotation(self):
        self.swapColor(U1, B4)  # U1 - B4
        self.swapColor(U3, B2)  # U3 - B2
        self.swapColor(B2, F3)  # B2 - F3
        self.swapColor(B4, F1)  # B4 - F1
        self.swapColor(B2, D3)  # B2 - D3
        self.swapColor(B4, D1)  # B4 - D1

        self.rightRotation('L')

        self.setProcedure('L')

    # 90 degrees left on L side
    def lprimeRotation(self):
        self.swapColor(F1, U1)  # F1 - U1
        self.swapColor(F3, U3)  # F3 - U3
        self.swapColor(F1, B4)  # F1 - B4
        self.swapColor(F3, B2)  # F3 - B2
        self.swapColor(F1, D1)  # F1 - D1
        self.swapColor(F3, D3)  # F3 - D3

        self.leftRotation('L')

        self.setProcedure('L\'')

    # 180 degrees right on L side
    def l2Rotation(self):
        self.lRotation()
        self.lRotation()
        self.setProcedure('L2')

    # 90 degrees right on U side
    def uRotation(self):
        self.swapColor(L1, F1)  # L1 - F1
        self.swapColor(L2, F2)  # L2 - F2
        self.swapColor(F1, B1)  # F1 - B1
        self.swapColor(F2, B2)  # F2 - B2
        self.swapColor(F1, R1)  # F1 - R1
        self.swapColor(F2, R2)  # F2 - R2

        self.rightRotation('U')

        self.setProcedure('U')

    # 90 degrees left on U side
    def uprimeRotation(self):
        self.swapColor(F1, R1)  # F1 - R1
        self.swapColor(F2, R2)  # F2 - R2
        self.swapColor(F1, B1)  # F1 - B1
        self.swapColor(F2, B2)  # F2 - B2
        self.swapColor(L1, F1)  # L1 - F1
        self.swapColor(L2, F2)  # L2 - F2

        self.leftRotation('U')

        self.setProcedure('U\'')

    # 180 degrees right on U side
    def u2Rotation(self):
        self.uRotation()
        self.uRotation()
        self.setProcedure('U2')

    # 90 degrees right on D side
    def dRotation(self):
        self.swapColor(F3, R3)  # F3 - R3
        self.swapColor(F4, R4)  # F4 - R4
        self.swapColor(F3, B3)  # F3 - B3
        self.swapColor(F4, B4)  # F4 - B4
        self.swapColor(F3, L3)  # F3 - L3
        self.swapColor(F4, L4)  # F4 - L4

        self.rightRotation('D')

        self.setProcedure('D')

    # 90 degrees left on D side
    def dprimeRotation(self):
        self.swapColor(F3, L3)  # F3 - L3
        self.swapColor(F4, L4)  # F4 - L4
        self.swapColor(F3, B3)  # F3 - B3
        self.swapColor(F4, B4)  # F4 - B4
        self.swapColor(F3, R3)  # F3 - R3
        self.swapColor(F4, R4)  # F4 - R4

        self.leftRotation('D')

        self.setProcedure('D\'')

    # 180 degrees right on D side
    def d2Rotation(self):
        self.dRotation()
        self.dRotation()
        self.setProcedure('D2')

    # 90 degrees right on F side
    def fRotation(self):
        self.swapColor(L2, U4)  # L2 - U4
        self.swapColor(L4, U3)  # L4 - U3
        self.swapColor(L2, R3)  # L2 - R3
        self.swapColor(L4, R1)  # L4 - R1
        self.swapColor(L2, D1)  # L2 - D1
        self.swapColor(L4, D2)  # L4 - D2

        self.rightRotation('F')

        self.setProcedure('F')

    # 90 degrees left on F side
    def fprimeRotation(self):
        self.swapColor(U3, L4)  # U3 - L4
        self.swapColor(U4, L2)  # U4 - L2
        self.swapColor(U3, D2)  # U3 - D2
        self.swapColor(U4, D1)  # U4 - D1
        self.swapColor(U3, R1)  # U3 - R1
        self.swapColor(U4, R3)  # U4 - R3

        self.leftRotation('F')

        self.setProcedure('F\'')

    # 180 degrees right on F side
    def f2Rotation(self):
        self.fRotation()
        self.fRotation()
        self.setProcedure('F2')

    # 90 degrees right on B side
    def bRotation(self):
        self.swapColor(U1, L3)  # U1 - L3
        self.swapColor(U2, L1)  # U2 - L1
        self.swapColor(U1, D4)  # U1 - D4
        self.swapColor(U2, D3)  # U2 - D3
        self.swapColor(U1, R2)  # U1 - R2
        self.swapColor(U2, R4)  # U2 - R4

        self.rightRotation('B')

        self.setProcedure('B')

    # 90 degrees left on B side
    def bprimeRotation(self):
        self.swapColor(U1, R2)  # U1 - R2
        self.swapColor(U2, R4)  # U2 - R4
        self.swapColor(U1, D4)  # U1 - D4
        self.swapColor(U2, D3)  # U2 - D3
        self.swapColor(U1, L3)  # U1 - L3
        self.swapColor(U2, L1)  # U2 - L1

        self.leftRotation('B')

        self.setProcedure('B\'')

    # 180 degrees right on B side
    def b2Rotation(self):
        self.bRotation()
        self.bRotation()
        self.setProcedure('B2')

    def rightRotation(self, color):
        if (color == 'U'):
            self.swapColor(U1, U2)
            self.swapColor(U1, U4)
            self.swapColor(U1, U3)
        elif (color == 'L'):
            self.swapColor(L1, L2)
            self.swapColor(L1, L4)
            self.swapColor(L1, L3)
        elif (color == 'F'):
            self.swapColor(F1, F2)
            self.swapColor(F1, F4)
            self.swapColor(F1, F3)
        elif (color == 'R'):
            self.swapColor(R1, R2)
            self.swapColor(R1, R4)
            self.swapColor(R1, R3)
        elif (color == 'B'):
            self.swapColor(B1, B2)
            self.swapColor(B1, B4)
            self.swapColor(B1, B3)
        elif (color == 'D'):
            self.swapColor(D1, D2)
            self.swapColor(D1, D4)
            self.swapColor(D1, D3)

    def leftRotation(self, color):
        if (color == 'U'):
            self.swapColor(U1, U3)
            self.swapColor(U1, U4)
            self.swapColor(U1, U2)
        elif (color == 'L'):
            self.swapColor(L1, L3)
            self.swapColor(L1, L4)
            self.swapColor(L1, L2)
        elif (color == 'F'):
            self.swapColor(F1, F3)
            self.swapColor(F1, F4)
            self.swapColor(F1, F2)
        elif (color == 'R'):
            self.swapColor(R1, R3)
            self.swapColor(R1, R4)
            self.swapColor(R1, R2)
        elif (color == 'B'):
            self.swapColor(B1, B3)
            self.swapColor(B1, B4)
            self.swapColor(B1, B2)
        elif (color == 'D'):
            self.swapColor(D1, D3)
            self.swapColor(D1, D4)
            self.swapColor(D1, D2)

    def swapColor(self, color1, color2):
        tmp = self.layout[color1]
        self.layout[color1] = self.layout[color2]
        self.layout[color2] = tmp

    def rotation(self, string):
        if (string == 'R'):
            self.rRotation()
        elif (string == 'R\''):
            self.rprimeRotation()
        elif (string == 'R2'):
            self.r2Rotation()
        elif (string == 'L'):
            self.lRotation()
        elif (string == 'L\''):
            self.lprimeRotation()
        elif (string == 'L2'):
            self.l2Rotation()
        elif (string == 'U'):
            self.uRotation()
        elif (string == 'U\''):
            self.uprimeRotation()
        elif (string == 'U2'):
            self.u2Rotation()
        elif (string == 'D'):
            self.dRotation()
        elif (string == 'D\''):
            self.dprimeRotation()
        elif (string == 'D2'):
            self.d2Rotation()
        elif (string == 'F'):
            self.fRotation()
        elif (string == 'F\''):
            self.fprimeRotation()
        elif (string == 'F2'):
            self.f2Rotation()
        elif (string == 'B'):
            self.bRotation()
        elif (string == 'B\''):
            self.bprimeRotation()
        elif (string == 'B2'):
            self.b2Rotation()
