#For high level coding

import os

from . import data

# For write-tree command
def write_tree (directory='.'):

    entries = []

    with os.scandir (directory) as it:
        for entry in it:

            #fetch directory of file in full
            full = f'{directory}/{entry.name}'

            #if directory is .codelog then
            if is_ignored (full):
                continue

            #Creates hash of each and every file
            if entry.is_file (follow_symlinks=False):

                type_ = 'blob'

                #Creates hash of each and every file
                with open (full, 'rb') as f:
                    oid = data.hash_object(f.read())
                    # print (data.hash_object (f.read ()), full)

            elif entry.is_dir (follow_symlinks=False):
                # write_tree (full)

                type_ = 'tree'
                oid = write_tree(full)
            entries.append((entry.name, oid, type_))

    tree = ''.join (f'{type_} {oid} {name}\n'
                    for name, oid, type_
                    in sorted (entries))
    return data.hash_object (tree.encode (), 'tree')



# For read-tree command (next 4 functions)

# to delete all existing thing before reading, so we dont have any older files after we read-tree
def _empty_current_directory ():
    for root, dirnames, filenames in os.walk ('.', topdown=False):
        for filename in filenames:
            path = os.path.relpath (f'{root}/{filename}')
            if is_ignored (path) or not os.path.isfile (path):
                continue
            os.remove (path)
        for dirname in dirnames:
            path = os.path.relpath (f'{root}/{dirname}')
            if is_ignored (path):
                continue
            try:
                os.rmdir (path)
            except (FileNotFoundError, OSError):
                # Deletion might fail if the directory contains ignored files,
                # so it's OK
                pass


# _iter_tree_entries is a generator that will take an OID of a tree, tokenize it line-by-line and yield the raw string values.
def _iter_tree_entries (oid):
    if not oid:
        return
    tree = data.get_object (oid, 'tree')
    for entry in tree.decode ().splitlines ():
        type_, oid, name = entry.split (' ', 2)
        yield type_, oid, name

# get_tree uses _iter_tree_entries to recursively parse a tree into a dictionary.
def get_tree (oid, base_path=''):
    result = {}
    for type_, oid, name in _iter_tree_entries (oid):
        assert '/' not in name
        assert name not in ('..', '.')
        path = base_path + name
        if type_ == 'blob':
            result[path] = oid
        elif type_ == 'tree':
            result.update (get_tree (oid, f'{path}/'))
        else:
            assert False, f'Unknown tree entry {type_}'
    return result

# read_tree uses get_tree to get the file OIDs and writes them into the working directory.
def read_tree (tree_oid):
    for path, oid in get_tree (tree_oid, base_path='./').items ():
        os.makedirs (os.path.dirname (path), exist_ok=True)
        with open (path, 'wb') as f:
            f.write (data.get_object (oid))





# commit command, takes message and int 'commit' txt it is stored such a way, first store key value then new line and then the message provided
def commit(info):
    commit = f'tree {write_tree ()}\n'
    commit += '\n'
    commit += f'{info}\n'

    return data.hash_object (commit.encode (), 'commit')





# it ignores the path of .codelog
def is_ignored(path):
    return any(ignored in path.split('/') for ignored in ['.codelog', '.git'])
