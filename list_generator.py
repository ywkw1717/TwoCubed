#!/usr/bin/env python

import re
from tqdm import tqdm

WORD_NUM = 5
proc = ['R', 'R\'', 'R2', 'L', 'L\'', 'L2', 'U', 'U\'', 'U2', 'D', 'D\'', 'D2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2']
procedure = []
optimization_list = ['RRRR', 'R\'R\'R\'R\'', 'R2R2', 'LLLL', 'L\'L\'L\'L\'', 'L2L2', 'UUUU', 'U\'U\'U\'U\'', 'U2U2', 'DDDD', 'D\'D\'D\'D\'', 'D2D2', 'FFFF', 'F\'F\'F\'F\'', 'F2F2', 'BBBB', 'B\'B\'B\'B\'', 'B2B2', 'RR\'', 'LL\'', 'UU\'', 'DD\'', 'FF\'', 'BB\'', 'R\'R', 'L\'L', 'U\'U', 'D\'D', 'F\'F', 'B\'B', 'RL\'', 'LR\'', 'UD\'', 'DU\'', 'FB\'', 'BF\'', 'L\'R', 'R\'L', 'D\'U', 'U\'D', 'B\'F', 'F\'B', 'R2L2', 'L2R2', 'U2D2', 'D2U2', 'F2B2', 'B2F2', 'RRR2', 'RR2R', 'R2RR', 'R\'R\'R2', 'R\'R2R\'', 'R2R\'R\'', 'LLL2', 'LL2L', 'L2LL', 'L\'L\'L2', 'L\'L2L\'', 'L2L\'L\'', 'UUU2', 'UU2U', 'U2UU', 'U\'U\'U2', 'U\'U2U\'', 'U2U\'U\'', 'DDD2', 'DD2D', 'D2DD', 'D\'D\'D2', 'D\'D2D\'', 'D2D\'D\'', 'FFF2', 'FF2F', 'F2FF', 'F\'F\'F2', 'F\'F2F\'', 'F2F\'F\'', 'BBB2', 'BB2B', 'B2BB', 'B\'B\'B2', 'B\'B2B\'', 'B2B\'B\'', 'RRL2', 'LLR2', 'UUD2', 'DDU2', 'FFB2', 'BBF2', 'R2LL', 'L2RR', 'U2DD', 'D2UU', 'F2BB', 'B2FF']

optimization_pattern = re.compile('|'.join(optimization_list))

def main():
    generator(proc, WORD_NUM)

    for i in procedure:
        print i


# procedure list generator
# increase procedure recursively
def generator(proc_list, depth):
    if (depth == 1):
        return ['R', 'R\'', 'R2', 'L', 'L\'', 'L2', 'U', 'U\'', 'U2', 'D', 'D\'', 'D2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2']

    recursive_list = []

    for proc_list_word in tqdm(proc_list):
        for proc_word in proc:
            # don't append useless factor
            if optimization_pattern.findall(proc_list_word.replace(' ', '') + proc_word):
                pass
            # append factor
            else:
                recursive_list.append(proc_list_word + ' ' + proc_word)
                procedure.append(proc_list_word + ' ' + proc_word)

    generator(recursive_list, depth - 1)

    return ['R', 'R\'', 'R2', 'L', 'L\'', 'L2', 'U', 'U\'', 'U2', 'D', 'D\'', 'D2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2'] + procedure


if __name__ == '__main__':
    main()
