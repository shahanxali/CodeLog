#For processing the user input, handles the commands

#argparse is for creating CLI commands, Program defining arguements and argparse parses it, here used for creating sub commands like git init or commit
#sys to read from the file, all text from file
import argparse
import sys

import os
from . import data
from . import base


def main ():
    args = parse_args ()
    args.func (args)


# Parse Arguements (parse = extracting meaningfull components) basic
# This function sets up the arguement parser for CLI (command line interface)
def parse_args ():
    parser = argparse.ArgumentParser ()

    commands = parser.add_subparsers (dest='command')
    commands.required = True

    # init setup
    init_parser = commands.add_parser ('init')
    init_parser.set_defaults (func=init)

    # hashing setup
    hash_object_parser = commands.add_parser ('hash-object')
    hash_object_parser.set_defaults (func=hash_object)
    hash_object_parser.add_argument ('file')

    # cat file setup
    cat_file_parser = commands.add_parser ('cat-file')
    cat_file_parser.set_defaults (func=cat_file)
    cat_file_parser.add_argument ('object')

    # write-tree setup
    write_tree_parser = commands.add_parser ('write-tree')
    write_tree_parser.set_defaults (func=write_tree)

    return parser.parse_args ()


# init command for my git, the function to tell what to do when init is called
def init (args):
    data.init ()
    print (f'Initialized empty CodeLog repository in {os.getcwd()}/{data.GIT_DIR}') #last one contains the info of directory


# Compute and prints the hash of the file
def hash_object (args):
    with open (args.file, 'rb') as f:
        print (data.hash_object (f.read ()))


# Computes hash value to find real one
def cat_file (args):
    sys.stdout.flush ()
    sys.stdout.buffer.write (data.get_object (args.object, expected = 'none'))

# Hashing for directories, basically for storing whole directory and not a single file
def write_tree (args):
    base.write_tree ()
