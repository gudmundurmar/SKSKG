# -*- coding: cp1252 -*-
from priority_dict import priority_dict


listi = []
b = False

def inputToDict(filename):
    dict = {}
    count = {}
    file = open(filename).readlines()
    for line in file:
        split = line.split(" ")
        if len(split) > 1:
            if '\n' in split[2]:
                split[2] = split[2][:-1]
        
            dict[split[0]].append([split[1],split[2]])
            dict[split[1]].append([split[0],split[2]])
        else:
            for i in range(0, int(split[0][:-1])):
                dict[str(i)] = [float("inf"), None]

    weight = MSTPRIM(dict,0, dict['0']); 
    print weight

    #listi.remove([None, '0'])
    listi.sort(key= lambda x:int(x[0]))
    for x in range(1,len(listi)):
        
        dict = {}
        for line in file:
            split = line.split(" ")
            if len(split) > 1:
                if '\n' in split[2]:
                    split[2] = split[2][:-1]
                if not(split[0]==listi[x][0] and split[1]==listi[x][1]):
                    dict[split[0]].append([split[1],split[2]])
                    dict[split[1]].append([split[0],split[2]])
            else:
                for i in range(0, int(split[0][:-1])):
                    dict[str(i)] = [float("inf"), None]

        weight = MSTPRIM(dict,0, dict['0']); 
        print listi[x][0],listi[x][1], weight


def MSTPRIM(G,w,r):
    r[0] = 0
    
    Q =  priority_dict(G);
    while Q:
        Q._rebuild_heap()
        #print Q
        
        u = Q.smallest()
        #print u
        global b
        if not b:
            if not u[0]==None and int(u[0])<int(u[1]):
                listi.append(u)
            else:
                v = [u[1],u[0]]
                listi.append(v)
        w += int(Q[u[1]][0])
        u = Q.pop_smallest()

        #print u

        for v in G[u]:
            if isinstance(v, list):
                stri = str(v[0])
                if v[0] in Q:
                    if float(v[1]) < float(Q[v[0]][0]):
                        Q[v[0]][1] = u
                        Q[v[0]][0] = float(v[1])
                        
    b = True               
    return w    
    
        


inputToDict("100.in")
