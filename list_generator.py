#!/usr/bin/env python

WORD_NUM = 1
proc = ['R', 'R\'', 'R2', 'L', 'L\'', 'L2', 'U', 'U\'', 'U2', 'D', 'D\'', 'D2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2']
procedure = []


def main():
    for proc_word in proc:
        print proc_word

    generator(proc, WORD_NUM)

    for i in procedure:
        print i


# procedure list generator
# increase procedure recursively
def generator(proc_list, depth):
    if (depth == 1):
        return ['R', 'R\'', 'R2', 'L', 'L\'', 'L2', 'U', 'U\'', 'U2', 'D', 'D\'', 'D2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2']

    recursive_list = []

    for proc_list_word in proc_list:
        for proc_word in proc:
            recursive_list.append(proc_list_word + proc_word)
            procedure.append(proc_list_word + proc_word)

    generator(recursive_list, depth - 1)

    return procedure


if __name__ == '__main__':
    main()
