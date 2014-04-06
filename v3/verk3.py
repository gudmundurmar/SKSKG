# -*- coding: cp1252 -*-
from priority_dict import priority_dict
from Queue import *
import time

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
                
            dict[split[0]].append([split[1], split[2]])
            dict[split[1]].append([split[0], split[2]])
                           
            notSpan.append([int(split[2]),split[0],split[1]])
        else:
            for i in range(0, int(split[0][:-1])):
                dict[str(i)] = [float("inf"), None, []]

    
    notSpan.sort(reverse=True)
    weight = MSTPRIM(dict,0, dict['0']);
    print weight
    NotMinPRIM(dict, weight)

tree = []


def MSTPRIM(G,w,r):
    global tree
    global notSpan
    r[0] = 0



    tree = []
    
    Q =  priority_dict(G);
    while Q:
        Q._rebuild_heap()
        
        u = Q.smallest()

        if not(Q[u][1] is None):
            if(int(u) < int(Q[u][1])):
                notSpan.remove([int(Q[u][0]), u,Q[u][1]])
            else:
                notSpan.remove([int(Q[u][0]), Q[u][1], u])
        
        w += int(Q[u][0])
        
        u = Q.pop_smallest()


        tree.append(u)
        
        for v in range(3,len(G[u])):
            ver = G[u][v]
            if ver[0] in Q:
                if float(ver[1]) < float(Q[ver[0]][0]):
                    Q[ver[0]][1] = u
                    G[ver[0]][1] = u

                    if float(G[u][0]) == float(0):
                        G[u][0] = float(ver[1])

                    #setur nýja besta
                    Q[ver[0]][0] = float(ver[1])
                    G[ver[0]][0] = float(ver[1])
    

    for i in range(1,len(tree)):
        G[str(G[tree[i]][1])][2].append(tree[i])

    
    return w    


def NotMinPRIM(G,w):

    
    cnt = 0
    nrSecond = 1

    weight = 0

    shortest = {}


    for i in range(1,len(tree)):
        
        node = tree[i]

        context = doubleBFS(G, node, G[node][1])
        
        for j in range(0,len(notSpan)):
            cur = len(notSpan)-1-j
            if notSpan[cur][1] in context and notSpan[cur][2] in context:
                continue
            elif notSpan[cur][1] in context or notSpan[cur][2] in context:
                weight = w-G[node][0]+notSpan[cur][0]
                break
        
        if(int(node) < int(G[node][1])):
            shortest[cnt] = [int(node), int(G[node][1]), int(weight)]
        else:
            shortest[cnt] = [int(G[node][1]), int(node), int(weight)]
        cnt += 1
        

    Q =  priority_dict(shortest);

    while Q:
        u = Q.smallest()
        print str(Q[u][0])+" "+str(Q[u][1])+" "+str(Q[u][2])
        u = Q.pop_smallest()
    

def doubleBFS(G,u,v):
    contextU = [u]
    contextV = [v]

    treeU = [u]
    treeV = [v]
    
    while treeU and treeV:
        curU = treeU.pop()
        for adjU in G[curU][2]:
            treeU.append(adjU)
            contextU.append(adjU)
        curV = treeV.pop()
        for adjV in G[curV][2]:
            treeV.append(adjV)
            contextV.append(adjV)

    result = []

    if len(contextU) < len(contextV):
        return contextU
    else:
        return contextV
        
        
    
                
start_time = time.time()
inputToDict("10k.in")
print time.time() - start_time, "seconds"
