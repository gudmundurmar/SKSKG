# -*- coding: cp1252 -*-
from priority_dict import priority_dict
from bisect import bisect_left
import time
import sys

class verk3:

    """
    FG:
    notSpan er listi sem inniheldur þá leggi sem eru ekki í minnsta spantrénu
    Span er listi inniheldur þá leggi sem eru í minnsta span trénu
    wholeNet er listi sem inniheldur alla leggi í netinu
    tree er listi sem inniheldur alla hnúta sem eru í minnsta span trénu
    """


    def __init__(self):
        self.notSpan = []
        self.Span = []
        self.wholeNet = []
        self.tree = []

    """
    Fyrir:  Ekkert
    Eftir:  Búið er að prenta út vigtina á minnsta spantrénu og næstminnsta
            spantré fyrir hvern legg
    """
    def inputToDict(self):
        dict = {}
        
        length = int(sys.stdin.readline())
        file = sys.stdin.readlines()
        for i in range(0, length):
            dict[str(i)] = [float("inf"), None, []]
        for line in file:
            
            split = line.split(" ")                   
            dict[split[0]].append([split[1], split[2]])
            dict[split[1]].append([split[0], split[2]])
            self.wholeNet.append([int(split[2]),split[0],split[1], False])

        self.wholeNet.sort()
        weight = self.MSTPRIM(dict, dict['0']);
        print weight
        self.NotMinPRIM(dict, weight)

    

    """
    Fyrir: G er net hnúta og r er upphafshnútur í netinu
    Eftir: Búið er að finna minnsta spantré fyrir G og vigt þess
    """
    def MSTPRIM(self,G,r):
   
        r[0] = 0

        w = 0
        
        Q =  priority_dict(G);
        while Q:
            Q._rebuild_heap()
            
            u = Q.pop_smallest()

            if not(G[u][1] is None):
                if(int(u) < int(G[u][1])):
                    self.Span.append([int(G[u][0]), u,G[u][1], False])
                else:
                    self.Span.append([int(G[u][0]), G[u][1], u, False])
            w += int(G[u][0])

            self.tree.append(u)
            
            for v in range(3,len(G[u])):
                ver = G[u][v]
                if ver[0] in Q:
                    if float(ver[1]) < float(Q[ver[0]][0]):
                        Q[ver[0]][1] = u
                        G[ver[0]][1] = u

                        if float(G[u][0]) == float(0):
                            G[u][0] = float(ver[1])

                        Q[ver[0]][0] = float(ver[1])
                        G[ver[0]][0] = float(ver[1])
        

        for i in range(1,len(self.tree)):
            G[str(G[self.tree[i]][1])][2].append(self.tree[i])

        return w    


    """
    Fyrir: G er net hnúta og w er vigt minnsta spantrés
    Eftir: Búið er að finna og prenta út N-1 minnstu spantrén.
    """
    def NotMinPRIM(self,G,w):

        self.Span.sort()
        for e in self.Span:
            res = binary_search(self.wholeNet, e)
            if not(res == -1):
                self.wholeNet[res][3] = True
            

        for e in range(0,len(self.wholeNet)):
            cur = len(self.wholeNet)-1-e
            if not(self.wholeNet[cur][3]):
                self.notSpan.append(self.wholeNet[cur])

        
        cnt = 0
        shortest = {}


        for i in range(1,len(self.tree)):
            
            node = self.tree[i]

            context = doubleBFS(G, node, G[node][1])
            
            for j in range(0,len(self.notSpan)):
                cur = len(self.notSpan)-1-j
                if self.notSpan[cur][1] in context and self.notSpan[cur][2] in context:
                    continue
                elif self.notSpan[cur][1] in context or self.notSpan[cur][2] in context:
                    weight = w-G[node][0]+self.notSpan[cur][0]
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


"""
Fyrir: G er net hnúta, u er hnútur og v er foreldi hnútsins í minnsta spantrénu
Eftir: Búið er að skipta minnsta  spantrénu upp í tvo samhengisþætti og finna minni samhengisþáttinn
"""
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


    if len(contextU) < len(contextV):
        return contextU
    else:
        return contextV
        


def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end    
    

if __name__ == '__main__':
    V3 = verk3()
    V3.inputToDict()

