# -*- coding: cp1252 -*-
from priority_dict import priority_dict


def inputToDict(filename):
    dict = {}
    count = {}
    file = open(filename).readlines()
    for line in file:
        split = line.split(" ")
        if len(split) > 1:
            if not split[0] in dict:
                dict[split[0]] = [float("inf"), None]
                dict[split[0]].append([split[1],split[2][:-1]])
            else:
                dict[split[0]].append([split[1],split[2][:-1]])

    weight = MSTPRIM(dict,0, dict['0']); 
    return weight


def MSTPRIM(G,w,r):
    r[0] = 0
    Q =  priority_dict(G);
    print Q
    while Q:
        u = Q.smallest()
        if 0 in Q:
            print "yeah"
        w += Q[u][0]
        u = Q.pop_smallest()

        for v in G[u]:
            if isinstance(v, list):
                print "ok"
                stri = str(v[0])
                print ''+stri
                if stri in Q and v[1] < Q[v[0]][0]:
                    print "common"
                    Q[v[0]][1] = u
                    Q[v[0]][0] = v[1]

    return w    
    
        


print inputToDict("test.in")
