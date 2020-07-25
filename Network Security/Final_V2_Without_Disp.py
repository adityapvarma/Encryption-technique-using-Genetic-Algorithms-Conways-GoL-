#Encoder V2 Without Disp
#Base V1 (Conways woth custom Key (Including hashing)
#Individual value for each squares. polyaphabetic done.
#Updated Rules

from copy import deepcopy
import hashlib


import pygame
from pygame.locals import *

from time import sleep,process_time

#Classes Used

class Sq(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf=pygame.Surface((5,5))
        self.surf.fill((255,255,255))
        self.rect=self.surf.get_rect()
        self.check=0
        self.value=0
        self.sub=0
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

def con_epoch(mat,obj):
    temp=deepcopy(mat)
    val_temp=deepcopy(mat)


    for i in range(len(mat)):
        for j in range(len(mat[i])):
            #print(i)
            neigh,lt_l=get_neigh(mat,(i,j),obj)
            temp[i][j],val_temp[i][j]=stat(neigh,obj[i][j].value,lt_l,obj[i][j].check)

    return temp,val_temp

def mutate(val):
    temp='{0:06b}'.format(val)

    if temp[-1]=='1':
        temp=temp[:-1]+'0'
    else:
        temp=temp[:-1]+'1'
    return temp

def crossover(l):
    lt=deepcopy(l)
    lt.sort()
    temp=''
    lt=['{0:06b}'.format(i) for i in lt]
    for i in range(len(lt)):
        temp+=lt[i][i*int(6/len(l)):int(6/len(l))*(i+1)]

    return int(temp,2)

def set_sub():

    for i in range(len(obj_list)):
        d={}
        for j in range(len(obj_list[i])):
            if obj_list[i][j].value not in d:
                d[obj_list[i][j].value]=0
            else:
                d[obj_list[i][j].value]+=1
            obj_list[i][j].sub=d[obj_list[i][j].value]
        
            

def stat(neigh,cur_val,lt_l,check):
    ct=neigh.count(1)
    holder=[]

    for i in lt_l:
        if i[0]==1:
            holder.append(i[1])
    
    #Updated Rules
            
    if ct==0:
        if check==0:
            return 0,cur_val
        else:
            #Mutation+Check 0
            return 0,mutate(cur_val)

    elif ct==1:
        if check==0:
            return 0,cur_val
        else:
            #Mutation+Check 1
            return 1,mutate(cur_val)

    elif ct==2:
        if check==0:
            #Crossover(2x1)+Check 1
            return 1,crossover(holder)
            
        else:
            #Crossover(2x1)+Check 1
            return 1,crossover(holder)

    elif ct==3:
        if check==0:
            #Crossover(3x1)+Check 1
            return 1,crossover(holder)
        else:
            #Crossover(3x1)+Check 1
            return 1,crossover(holder)

    elif ct==4:
        if check==0:
            return 0,cur_val
        else:
            return 0,cur_val

    elif ct in [5,6,7,8]:
        return 0,cur_val


def get_neigh(mat,ind,obj):
    l=[(ind[0]+i,ind[1]+j) for i in range(-1,2) for j in range(-1,2)]
    lt=[]
    lt_l=[]
    l.pop(l.index(ind))

    for i in l:
        if i[0] in range(len(mat)) and i[1] in range(len(mat[0])):
            lt.append(i)
    ltp=[mat[i[0]][i[1]] for i in lt]
    #lt_l=[[[i[0],i[1]],[mat[i[0]][i[1]]]] for i in lt]
    #lt_l=[[mat[i[0]][i[1]],obj[i[0]][i[1]].value] for i in lt]
    lt_l=[[mat[i[0]][i[1]],obj[i[0]][i[1]].value] for i in lt]
    
    #print(ltp)
    return ltp,lt_l

def init_set_stat(stat_list):
    for i in range(len(stat_list)):
        for j in range(len(stat_list[i])):
            obj_list[i][j].stat(stat_list[i][j])
            #print(a.lt[i][j].check)

def set_stat(stat_list,val_list):
    for i in range(len(stat_list)):
        for j in range(len(stat_list[i])):
            obj_list[i][j].stat(stat_list[i][j])

            if isinstance(val_list[i][j],str):
                val_list[i][j]=int(val_list[i][j],2)
            obj_list[i][j].value=val_list[i][j]
            #print(obj_list[i][j].value)
            #print(a.lt[i][j].check)

def disp_count(ep_count):
    text_surf=font.render("Epoch Count :"+str(ep_count),True,(255,255,255))
    text=text_surf.get_rect()
    text.topleft=(10,10)
    screen.blit(text_surf,text)

def conv_mat(l,n):
    return [l[i:i+n] for i in range(0,len(l),n)]

def Run_Epoch():
    ep_count=0
    for i in range(iter_no):
        ep_count+=1
        cp,temp_val=con_epoch(cp,obj_list)
        set_stat(cp,temp_val)
        blit_all()
        disp_count(ep_count)
        pygame.display.flip()
        #sleep(1)
    
    
    

#End of Function Defs
##################################


#Main
##pygame.init()
run=True

#Background
##bg=pygame.Surface((1600,900))
##bg.fill((0,0,0))

#Epoch Count
##font=pygame.font.Font("Dosis-Bold.ttf",15)

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
key=input("Enter Key (<Keyword>-<iter_no>) :")


pt=input("Enter Plain text :")
pt=pt.upper()

init_time=process_time()

q=key.split('-')
iter_no=int(q[1])
key=q[0]

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

##screen=pygame.display.set_mode((800,800))


"""
print("Starting Condition")
for i in init_state:
    print(i)
print("")
"""

#First Disp
#screen.blit(bg,(0,0))
init_set_stat(init_state)
##blit_all()
"""
text_surf=font.render("0",True,(255,255,255))
text=text_surf.get_rect()
text.center=(10,10)
screen.blit(text_surf,text)
"""
##disp_count(0)
##pygame.display.flip()


cp=deepcopy(init_state)


#Infi-Loop for complete Exec
#while run:


over_ct=0
en_text=''
key=key.upper()

#check -1
while over_ct<len(pt):
    #Run_Epoch()
    ep_count=0
    for i in range(iter_no):
        ep_count+=1
        cp,temp_val=con_epoch(cp,obj_list)
        set_stat(cp,temp_val)
        ##blit_all()
        ##disp_count(ep_count)
        ##pygame.display.flip()
        #sleep(1)    

    
    set_sub()
    for i in key:
        if over_ct<len(pt):
            r=ord(i)-32
            c=ord(pt[over_ct])-32
            #print(r,c)

            temp_val=chr(obj_list[r][c].value+32)
            temp_sub=obj_list[r][c].sub
            en_text+=(temp_val+str(temp_sub)+"|")
            over_ct+=1

en_text=en_text[:-1]
print(en_text)
print(process_time()-init_time)

##pygame.quit()
    
    
    



