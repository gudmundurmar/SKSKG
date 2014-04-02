# -*- coding: cp1252 -*-
from priority_dict import priority_dict


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
    return weight


def MSTPRIM(G,w,r):
    r[0] = 0
    Q =  priority_dict(G);
    while Q:

        print Q
        
        u = Q.smallest()
        print u
        w += int(Q[u][0])
        u = Q.pop_smallest()

        for v in G[u]:
            if isinstance(v, list):
                stri = str(v[0])
                if v[0] in Q:
                    if float(v[1]) < float(Q[v[0]][0]):
                        Q[v[0]][1] = u
                        Q[v[0]][0] = float(v[1])

    return w    
    
        


print inputToDict("test.in")