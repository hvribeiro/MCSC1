#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Double a number.')

parser.add_argument("x", help="value to double",type=float)

args = parser.parse_args()

print(args.x**2)