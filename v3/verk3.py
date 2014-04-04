# -*- coding: cp1252 -*-
from priority_dict import priority_dict

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
                dict[str(i)] = [float("inf"), None]

    weight = MSTPRIM(dict,0, dict['0']);
    print weight
    NotMinPRIM(weight)
    #return weight


def MSTPRIM(G,w,r):
    global notSpan
    global Span

    
    r[0] = 0
    Q =  priority_dict(G);
    while Q:
        Q._rebuild_heap()
        
        u = Q.smallest()

        if(not(int(u) == 0)):
            if(int(u) < int(Q[u][1])):
                Span.append([Q[u][1],u,int(Q[u][0])])
                notSpan.remove([str(u),str(Q[u][1]),str(int(Q[u][0]))])
            else:
                Span.append([Q[u][1],u,int(Q[u][0])])
                notSpan.remove([str(Q[u][1]),str(u),str(int(Q[u][0]))])
        
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


def NotMinPRIM(w):
    global Span
    global notSpan

    print Span

    check = 0
    minEdge = [-1,-1,float("inf")]
    checkedVertices = []
    output = ""
    invalidMin = True

    for e in Span:

        
        
        newWeight = w-e[2]
        check = 1
        output = str(e[0])+" "+str(e[1])+" "
        for v in Span:
            if str(e[1]) == str(v[0]):
                check = 0

        if(check == 1):
            checkedVertices.append(str(e[0]))
            checkedVertices.append(str(e[1]))
        else:
            checkedVertices.append(str(e[0]))

        for notUsed in notSpan:
            if e[check] == notUsed[0] or e[check] == notUsed[1]:
                if float(notUsed[2]) < float(minEdge[2]):
                    invalidMin = False
                    minEdge = notUsed
        print checkedVertices
        #print "this is e: "+str(e)
        #print notSpan
        #print minEdge

        newWeight += int(minEdge[2])
        output += str(newWeight)

        print output

        for i in notSpan:
            print i

        print "this is span: "+str(notSpan)

        for nUsed in notSpan:
            print nUsed
            if (nUsed[0] in checkedVertices) and (nUsed[1] in checkedVertices):
                #print "to remove: "+str(notUsed)
                notSpan.remove(nUsed);
                if nUsed == minEdge:
                    invalidMin = True
                    minEdge = [-1,-1,float("inf")]
                    
        if invalidMin:
            for findMin in notSpan:
                    if float(findMin[2]) < minEdge[2]:
                        invalidMin = False            
                        minEdge = findMin
        

                

        

        
                
        
                
        


inputToDict("test.in")
