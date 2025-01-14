# def main():
#     print("Hello World!")



#argparse is for creating CLI commands, Program defining arguements and argparse parses it, here used for creating sub commands like git init or commit
import argparse

import os
from . import data


def main ():
    args = parse_args ()
    args.func (args)


def parse_args ():
    parser = argparse.ArgumentParser ()

    commands = parser.add_subparsers (dest='command')
    commands.required = True

    init_parser = commands.add_parser ('init')
    init_parser.set_defaults (func=init)

    return parser.parse_args ()


def init (args):

    data.init ()
    print (f'Initialized empty CodeLog repository in {os.getcwd()}/{data.GIT_DIR}') #last one contains the info of directory
