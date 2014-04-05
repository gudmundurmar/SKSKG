# -*- coding: cp1252 -*-
from priority_dict import priority_dict
from Queue import *

notSpan = []
Span = []

notSpan = []
Span = []


def inputToDict(filename):
    global notSpan
    global Span
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

            notSpan.append([split[0],split[1],split[2]])
        else:
            for i in range(0, int(split[0][:-1])):
                dict[str(i)] = [float("inf"), float("inf"), None, []]

    weight = MSTPRIM(dict,0, dict['0']);
    print weight
    #print dict
    #maxx = BFSFillMax(dict,weight)
    NotMinPRIM(dict, weight)
    #MaxPrims(dict, maxx)


tree = []


def MSTPRIM(G,w,r):
    global tree
    global Span

    r[0] = 0

    next = 0

    tree = []
    Span = []
    
    Q =  priority_dict(G);
    while Q:
        Q._rebuild_heap()
        
        u = Q.smallest()

        
        w += int(Q[u][0])
        
        u = Q.pop_smallest()


        #finnur næst besta 

        print next
        #if not(u == next):
        if Q:
            next = Q.smallest()
            secondBest = G[next][0]

        Span.append(secondBest)

        
        print u
        print Span
        print ""

        tree.append(u)
        
        #print u
        for v in range(4,len(G[u])):
            ver = G[u][v]
            #print ver
            #print Q
            if ver[0] in Q:
                if float(ver[1]) < float(Q[ver[0]][0]):
                    Q[ver[0]][2] = u
                    G[ver[0]][2] = u

                    """if float(G[u][0]) == float(0):
                        G[u][0] = float(ver[1])"""
                        
                    #setur það sem var best í næst besta
                    """Q[ver[0]][1] = Q[ver[0]][0]
                    G[ver[0]][1] = Q[ver[0]][0]"""

                    #setur nýja besta
                    Q[ver[0]][0] = float(ver[1])
                    G[ver[0]][0] = float(ver[1])
                """elif float(ver[1]) < float(Q[ver[0]][1]):
                    #ef að það þarf bara að breyta næstbesta
                    Q[ver[0]][1] = float(ver[1])
                    G[ver[0]][1] = float(ver[1])"""

        

            
    #print G#print G
    print tree

    """for i in range(1,len(tree)):
        if G[tree[i]][2] > tree[i]:
            Span.append([tree[i],G[tree[i]][2]])
        else:
            Span.append([G[tree[i]][2], tree[i]])
        G[str(G[tree[i]][2])][3].append(tree[i])

    for i in range(1,len(tree)):
        G[str(tree[i])][3].append(str(G[tree[i]][2]))"""

    #print Span
    """for u in tree:
        if float(G[ver[0]][0]) < float(ver[1]):
            if float(ver[1]) < float(G[ver[0]][1]):
                G[ver[0]][1] = float(ver[1])"""

    #færa gildi frá barni yfir til foreldris, ef það er til styttri leið

    
    return w    



def NotMinPRIM(G,w):

    
    cnt = 0
    nrSecond = 1

    shortest = {}

        
        toRemove = []

    for e in tree:
        if not(str(e) == str(0)):
            weight = w-G[e][0]+Span[nrSecond]
            nrSecond += 1
            if(e < G[e][2]):
                shortest[cnt] = [int(e), int(G[e][2]), int(weight)]
            else:
                shortest[cnt] = [int(G[e][2]), int(e), int(weight)]
            cnt += 1

    Q =  priority_dict(shortest);

    while Q:
        u = Q.smallest()
        print str(Q[u][0])+" "+str(Q[u][1])+" "+str(Q[u][2])
        u = Q.pop_smallest()
    
        
                


inputToDict("simple.in")

