#Key Hashing
#input key converted to 64*64 bits for conways initial condition

import hashlib
from copy import deepcopy




key=input()

key_mod_=[]
key_mod=''
temp=deepcopy(key)


while len(key_mod)<64*64:
    temp=hashlib.sha512(temp.encode())
    h='{0:08b}'.format(int(temp.hexdigest(),16))
    h_=[i for i in h]
    #print(h)
    key_mod+=h
    key_mod_.extend(h_)
    temp=h

key_mod=key_mod[:64*64]
key_mod_=key_mod_[:64*64]
    

    
    
    
    
    
