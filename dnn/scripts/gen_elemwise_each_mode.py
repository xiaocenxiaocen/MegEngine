#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse

from gen_elemwise_utils import ARITIES, MODES

def main():
    parser = argparse.ArgumentParser(
        description='generate elemwise each mode',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('output', help='output directory')
    args = parser.parse_args()


    with open(args.output, 'w') as fout:
        w = lambda s: print(s, file=fout)
        w('// generated by gen_elemwise_each_mode.py')
        keys = list(MODES.keys())
        keys.sort()
        for (anum, ctype) in keys:
            w('#define MEGDNN_FOREACH_ELEMWISE_MODE_{}_{}(cb) \\'.format(
                ARITIES[anum], ctype))
            for mode in MODES[(anum, ctype)]:
                w('    MEGDNN_ELEMWISE_MODE_ENABLE({}, cb) \\'.format(mode))
            w('')

    print('generated each_mode.inl')
    os.utime(args.output)

if __name__ == '__main__':
    main()
