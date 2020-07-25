#Base V1 (Conways woth custom Key (Including hashing)
#Individual value for each squares. polyaphabetic done.
#Updated Rules

from copy import deepcopy
import hashlib


import pygame
from pygame.locals import *

from time import sleep

#Classes Used

class Sq(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf=pygame.Surface((5,5))
        self.surf.fill((255,255,255))
        self.rect=self.surf.get_rect()
        self.check=0
        self.value=0
#
    def stat(self,val):
        if val:
            self.surf.fill((255,255,255))
            #print("On")
        else:
            self.surf.fill((0,0,0))
            #print("Off")
        self.check=val


class Mat():
    def __init__(self,dim):
        self.lt=[[Sq() for i in range(dim[1])] for j in range(dim[0])]
        self.assign()
        
    def assign(self):
        for i in range(len(self.lt)):
            for j in range(len(self.lt[i])):
                self.lt[i][j].rect.center=(50+10*j,50+10*i)
                self.lt[i][j].value=(i+j)%64

#End of Class Defs
##############################


#Functions

def blit_all():
    screen.blit(bg,(0,0))
    for i in obj_list:
        for j in i:
            screen.blit(j.surf,j.rect)
            #print(j.rect.center)

def con_epoch(mat):
    temp=deepcopy(mat)
    print(type(temp))

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            neigh=get_neigh(mat,(i,j))
            temp[i][j]=stat(neigh)

    return temp


def stat(neigh):
    ct=neigh.count(1)

    #Updated Rules
    """
    if ct>=4:
        return 0
    else:
        if ct==0:
    """

    

    if ct==0:
        #No change 
        return 0
    
            
    if ct in [2,3]:
        return 1
    else:
        return 0
    
    

def get_neigh(mat,ind):
    l=[(ind[0]+i,ind[1]+j) for i in range(-1,2) for j in range(-1,2)]
    lt=[]
    lt_l=[]
    l.pop(l.index(ind))

    for i in l:
        if i[0] in range(len(mat)) and i[1] in range(len(mat[0])):
            lt.append(i)
    ltp=[mat[i[0]][i[1]] for i in lt]
    lt_l=[[[i[0],i[1]],[mat[i[0]][i[1]]]] for i in lt]
    #print(ltp)
    return ltp

def set_stat(stat_list):
    for i in range(len(stat_list)):
        for j in range(len(stat_list[i])):
            obj_list[i][j].stat(stat_list[i][j])
            #print(a.lt[i][j].check)
            

def disp_count():
    text_surf=font.render("Epoch Count :"+str(ep_count),True,(255,255,255))
    text=text_surf.get_rect()
    text.topleft=(10,10)
    screen.blit(text_surf,text)

def conv_mat(l,n):
    return [l[i:i+n] for i in range(0,len(l),n)]
    

#End of Function Defs
##################################


#Main
pygame.init()
run=True

#Background
bg=pygame.Surface((1600,900))
bg.fill((0,0,0))

#Epoch Count
font=pygame.font.Font("Dosis-Bold.ttf",15)

"""
init_state=[
    [1,1,0,0,0],
    [0,1,0,1,0],
    [0,0,1,1,1],
    [0,0,0,1,0],
    [1,0,0,0,0]]
"""
#Key Hashing with SHA512 to define Init state of Conway

#Key Input
key=input("Enter Key :")  

key_mod_=[]
key_mod=''
temp=deepcopy(key)


while len(key_mod)<64*64:
    temp=hashlib.sha512(temp.encode())
    h='{0:08b}'.format(int(temp.hexdigest(),16))
    h_=[int(i) for i in h]
    #print(h)
    key_mod+=h
    key_mod_.extend(h_)
    temp=h

key_mod=key_mod[:64*64]
key_mod_=key_mod_[:64*64]

init_state=conv_mat(key_mod_,64)

    

siz_a,siz_b=len(init_state),len(init_state[0])
a=Mat((siz_a,siz_b))
obj_list=a.lt

screen=pygame.display.set_mode((800,800))
ep_count=0

"""
print("Starting Condition")
for i in init_state:
    print(i)
print("")
"""

#First Disp
#screen.blit(bg,(0,0))
set_stat(init_state)
blit_all()
"""
text_surf=font.render("0",True,(255,255,255))
text=text_surf.get_rect()
text.center=(10,10)
screen.blit(text_surf,text)
"""
disp_count()
pygame.display.flip()


cp=deepcopy(init_state)


#Infi-Loop for complete Exec
while run:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                run=False
        elif event.type==QUIT:
            run=False

    kp=pygame.key.get_pressed()
    if kp[K_TAB]:
        ep_count+=1
        cp=con_epoch(cp)
        set_stat(cp)
        blit_all()
        disp_count()
        pygame.display.flip()
        sleep(0.2)
    

pygame.quit()

"""
for i in obj_list:
    for j in i:
        print(j.value, end=' ')
    print()

    
"""
