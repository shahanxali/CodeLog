#For manipulation of directories and working realted to system

import hashlib
import os


GIT_DIR = '.codelog'

#created directory (.codelog (.git))
def init ():
    os.makedirs (GIT_DIR)
    os.makedirs (f'{GIT_DIR}/objects') # creation of directory to store hashes


# Creation of OID (the SHA1 key)
def hash_object (data):
    oid = hashlib.sha1 (data).hexdigest ()
    with open (f'{GIT_DIR}/objects/{oid}', 'wb') as out:
        out.write (data)
    return oid


# reads the OID, the cat-file, reverse of hashing
def get_object (oid):
    with open (f'{GIT_DIR}/objects/{oid}', 'rb') as f:
        return f.read ()
