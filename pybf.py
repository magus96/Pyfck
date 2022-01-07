#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[2]:


def runcode(file):
    f=open(file,'r')
    evaluate(f.read())
    f.close()
    
    


# In[5]:


def evaluate(bfcode):
    bracks=brackify(bfcode)
    cells=[0]
    code_ptr=0
    cell_ptr=0
    
    while code_ptr<len(bfcode):
        inst=bfcode[code_ptr]
        
        if inst=='>':
            cell_ptr+=1
            if cell_ptr==len(cells):
                cells.append(0)
                
        if inst=='<':
            cell_ptr=0 if cell_ptr<=0 else cell_ptr-1
        
        if inst=='+':
            cells[cell_ptr]=(cells[cell_ptr]+1)%255
            
        if inst=='-':
            cells[cell_ptr]=(cells[cell_ptr]-1)%255
            
        if inst=='[' and cells[cell_ptr]==0:
            code_ptr=brackify(code_ptr)
            
        if inst==']' and cells[cell_ptr]!=0:
            code_ptr=brackify(code_ptr)
            
        if inst=='.':
            sys.stdout.write(chr(cells[cell_ptr]))
            
        if inst==',':
            sys.stdout.write('\n')
            c=ord(input('>0')[0])
            cells[cell_ptr]=c
            
        code_ptr+=1
        
            
    


# In[6]:


def brackify(bfcode):
    stack=[]
    brackmap={}
    
    for position,command in enumerate(bfcode):
        if command=='[':
            stack.append(position)
            
        if command==']':
            start=stack.pop()
            brackmap[start]=position
            brackmap[position]=start
            
    return brackmap       


# In[7]:


def main():
    if len(sys.argv)==2:
        runcode(sys.argv[1])
    else:
        print("usage {} file".format(sys.argv[0]))
        
        


# In[8]:


if __name__=="__main__":
    main()


# In[ ]:




