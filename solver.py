#!/usr/bin/env python
# coding: utf-8

import ConfigParser

inifile = ConfigParser.SafeConfigParser()
inifile.read('./config.ini')

U = inifile.get('settings', 'U')
D = inifile.get('settings', 'D')
R = inifile.get('settings', 'R')
L = inifile.get('settings', 'L')
F = inifile.get('settings', 'F')
B = inifile.get('settings', 'B')

def main():
    print U, D, R, L, F, B


if __name__ == '__main__':
    main()
