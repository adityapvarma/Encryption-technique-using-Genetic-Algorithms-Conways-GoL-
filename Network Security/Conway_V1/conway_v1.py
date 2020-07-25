#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Conways Game V1


# In[ ]:


from copy import deepcopy


# In[ ]:


def con_epoch(mat):
    temp=deepcopy(mat)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            neigh=get_neigh(mat,(i,j))
            #print(i," ",j," ",neigh)
            temp[i][j]=stat(neigh)
            """
            print("Check")
            for k in mat:
                print(k)
            
            print("\n")
            """
    
    return temp


# In[ ]:


def stat(neigh):
    ct=neigh.count(1)
    #print(ct)
    
    if ct>3:
        return 0
    elif ct in [2,3]:
        return 1
    else:
        return 0
    


# In[ ]:


def get_neigh(mat,ind):
    l=[(ind[0]+i,ind[1]+j) for i in range(-1,2) for j in range (-1,2)]
    lt=[]
    l.pop(l.index(ind))
    for i in l:
        if i[0] in range(len(mat)) and i[1] in range(len(mat[0])):
            lt.append(i)
    #print(lt)
    ltp=[mat[i[0]][i[1]] for i in lt]
    return ltp
    

"""
# In[ ]:

a=[[1,2,3],[4,5,6],[7,8,9]]
print(get_neigh(a,(2,0)))


# In[ ]:


for i in range(len(a)):
    for j in range(len(a[i])):
        temp=get_neigh(a,(i,j))
        print("Neighbour of ",a[i][j]," : ",temp)

"""
# In[ ]:


l1=[
    [1,1,0],
    [0,1,0],
    [0,0,1]]

print("Starting Condition")
for i in l1:
    print(i)
print("")

cp=deepcopy(l1)

while True:
    cp=con_epoch(cp)
    for i in cp:
        print(i)

    a=input()
    
    


# In[ ]:




