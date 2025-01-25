#For processing the user input, handles the commands

#argparse is for creating CLI commands, Program defining arguements and argparse parses it, here used for creating sub commands like git init or commit
#sys to read from the file, all text from file
import argparse
import sys

#textwrap for log command
import textwrap

import os
from . import data
from . import base


def main ():
    args = parse_args()
    args.func (args)


# Parse Arguements (parse = extracting meaningfull components) basic
# This function sets up the arguement parser for CLI (command line interface)
def parse_args():
    parser = argparse.ArgumentParser ()

    commands = parser.add_subparsers (dest='command')
    commands.required = True

    # init setup
    init_parser = commands.add_parser ('init')
    init_parser.set_defaults (func=init)

    # hash-object setup
    hash_object_parser = commands.add_parser ('hash-object')
    hash_object_parser.set_defaults (func=hash_object)
    hash_object_parser.add_argument ('file')

    # cat-file setup
    cat_file_parser = commands.add_parser ('cat-file')
    cat_file_parser.set_defaults (func=cat_file)
    cat_file_parser.add_argument ('object')

    # write-tree setup
    write_tree_parser = commands.add_parser ('write-tree')
    write_tree_parser.set_defaults (func=write_tree)

    # read-tree setup
    read_tree_parser = commands.add_parser('read-tree')
    read_tree_parser.set_defaults(func = read_tree)
    read_tree_parser.add_argument('tree')

    # commit setup
    commit_parser = commands.add_parser ('commit')
    commit_parser.set_defaults (func = commit)
    commit_parser.add_argument ('-m', '--message', required=True)

    # log setup
    log_parser = commands.add_parser ('log')
    log_parser.set_defaults (func=log)
    log_parser.add_argument ('oid', nargs='?')


    return parser.parse_args ()


#Main function what to do when the codelog is called

# init command for my git
def init (args):
    data.init ()
    print (f'Initialized empty CodeLog repository in {os.getcwd()}/{data.GIT_DIR}') #last one contains the info of directory


# Compute and prints the hash of the file
def hash_object (args):
    with open (args.file, 'rb') as f:
        print (data.hash_object (f.read ()))


# Computes hash value to find real one
def cat_file(args):
    # Allow any object type by setting expected=None, added this to see commit's oid, hash
    obj = data.get_object(args.object, expected=None)
    sys.stdout.flush()
    sys.stdout.buffer.write(obj)


# Hashing for directories, basically for storing whole directory and not a single file
def write_tree (args):
    ## base.write_tree ()
    print(base.write_tree());

# Reading the hash of a directory (created by write tree)
def read_tree(args):
    base.read_tree(args.tree)


# Commit command to attach other information WE want to provide like date or time or any messages
def commit (args):
    print (base.commit (args.message))


# Log command to print all the previous commits
def log (args):
    oid = args.oid or data.get_HEAD ()
    oid = data.get_HEAD ()
    while oid:
        commit = base.get_commit (oid)

        print (f'commit {oid}\n')
        print (textwrap.indent (commit.message, '    '))
        print ('')

        oid = commit.parent
