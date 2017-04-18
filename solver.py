#!/usr/bin/env python
# coding: utf-8

import ConfigParser

inifile = ConfigParser.SafeConfigParser()
inifile.read('./config.ini')


class Cube:
    """ The Cube Class"""
    """ solved cube layout is UUUULLLLFFFFRRRRBBBBDDDD """

    # コンストラクタ
    def __init__(self, layout):
        self.layout = list(layout)  # 文字列をリストに変換
        self.colors = [
            inifile.get('settings', 'U'),
            inifile.get('settings', 'L'),
            inifile.get('settings', 'F'),
            inifile.get('settings', 'R'),
            inifile.get('settings', 'B'),
            inifile.get('settings', 'D')
        ]

    def getLayout(self):
        return self.layout

    def getColor(self, num):
        return self.colors[num]


def main():
    cube = Cube('BUFFDDLLRRDFURDFBRLUBLBU')
    print 'U: ' + cube.getColor(0)
    print cube.getLayout()


if __name__ == '__main__':
    main()
