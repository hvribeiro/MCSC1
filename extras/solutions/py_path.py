#!/usr/bin/env python

"""Script to search the PYTHONPATH for a module"""

import os
import sys
import glob
import argparse

def find_module(module):
    result = []
    # Loop over the list of paths in sys.path
    for subdir in sys.path:
        # Join the subdir path with the module we're searching for
        pth = os.path.join(subdir, module)
        # Use glob to test if the pth is exists
        res = glob.glob(pth)
        # glob returns a list, if it is not empty, the pth exists
        if len(res) > 0:
            result.append(res)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search in $PYTHONPATH for a module.')
    parser.add_argument("name", help="module name",type=str)
    args = parser.parse_args()

    result = find_module(args.name)
    print(result)