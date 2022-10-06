def flatten(x):
    
    for i in x:
        if isinstance(i,list):
            flatten(i)
        else:
            l1.append(i)
    
    

l= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l1 = [] 
flatten(l)
print(l1)