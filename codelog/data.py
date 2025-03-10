#For manipulation of directories and working realted to system

import hashlib
import os


GIT_DIR = '.codelog'

#created directory (.codelog (.git))
def init ():
    os.makedirs (GIT_DIR)
    os.makedirs (f'{GIT_DIR}/objects') # creation of directory to store hashes


# HEAD to store previous commits
def set_HEAD (oid):
    with open (f'{GIT_DIR}/HEAD', 'w') as f:
        f.write (oid)

# function to find out the head, parent
def get_HEAD ():
    if os.path.isfile (f'{GIT_DIR}/HEAD'):
        with open (f'{GIT_DIR}/HEAD') as f:
            return f.read ().strip ()


# Creation of OID (the SHA1 key)
def hash_object (data, type_='blob'):

    #specifying object type
    obj = type_.encode () + b'\x00' + data
    oid = hashlib.sha1 (obj).hexdigest ()

    #oid writing
    with open (f'{GIT_DIR}/objects/{oid}', 'wb') as out:
        out.write (obj)
    return oid



# reads the OID, the cat-file, reverse of hashing
def get_object (oid, expected='blob'):

    #for reading hash
    with open (f'{GIT_DIR}/objects/{oid}', 'rb') as f:
        obj = f.read ()

    #for reading type of object
    type_, _, content = obj.partition (b'\x00')
    type_ = type_.decode ()

    #if type is given, not default
    if expected is not None:
        assert type_ == expected, f'Expected {expected}, got {type_}'
    return content
