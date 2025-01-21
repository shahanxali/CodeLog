#For high level coding

import os

from . import data


def write_tree (directory='.'):
    with os.scandir (directory) as it:
        for entry in it:

            #fetch directory of file in full
            full = f'{directory}/{entry.name}'

            #if directory is .codelog then
            if is_ignored (full):
                continue

            #Creates hash of each and every file
            if entry.is_file (follow_symlinks=False):
                #Creates hash of each and every file
                with open (full, 'rb') as f:
                    print (data.hash_object (f.read ()), full)

            elif entry.is_dir (follow_symlinks=False):
                write_tree (full)

    # TODO actually create the tree object

# it ignores the path of .codelog
def is_ignored (path):
    return '.codelog' in path.split ('/')
