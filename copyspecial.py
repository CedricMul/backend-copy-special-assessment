#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import os.path
import shutil
import subprocess
import argparse
import sys

# This is to help coaches and graders identify student assignments
__author__ = "Cedric Mulvihill"


# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
    ditectory_list = os.listdir(dir)
    special_list = []
    literal_special = re.compile(r'__[a-zA-Z0-9]+[-_]*[a-zA-Z0-9]*__')
    for i in ditectory_list:
        if literal_special.search(i):
            path = os.path.abspath(i)
            special_list.append(path)
    return special_list


def copy_to(paths, dir):
    if '/' in dir:
        split_directory = dir.split('/')
        split_directory.pop()
        if len(split_directory) > 1:
            directory_path = split_directory.join('/')
        else:
            directory_path = split_directory[0]
    else:
        directory_path = dir
    
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path)
    for a in paths:
        shutil.copy(a, dir)

def zip_to(paths, zippath):
    command_string = 'zip -j zipfile'
    for p in paths:
        command_string += ' ' + p
    print("Executing command: " + command_string)
    os.system(command_string)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('--from_dir', help='return list of special files from dir')
    parser.add_argument('dir', help='a single directory search', nargs='?')
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit()

    if not args.from_dir:
        x = get_special_paths(args.dir)
        for i in x:
            print(i)
    else:
        from_paths = get_special_paths(args.from_dir)
        if args.todir:
            copy_to(from_paths, args.todir)
        elif args.tozip:
            zip_to(from_paths, args.tozip)
        else:
            parser.print_usage()




    
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
