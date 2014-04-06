from priority_dict import priority_dict

"""MinimumSpanningTree.py

Kruskal's algorithm for minimum spanning trees. D. Eppstein, April 2006.
"""

from UnionFind import UnionFind

def MinimumSpanningTree(G):
    """
    Return the minimum spanning tree of an undirected graph G.
    G should be represented in such a way that G[u][v] gives the
    length of edge u,v, and G[u][v] should always equal G[v][u].
    The tree is returned as a list of edges.
    """
    
    # Kruskal's algorithm: sort edges by weight, and add them one at a time.
    # We use Kruskal's algorithm, first because it is very simple to
    # implement once UnionFind exists, and second, because the only slow
    # part (the sort) is sped up by being built in to Python.
    subtrees = UnionFind()
    tree = []
    edges = [(G[u][v],u,v) for u in G for v in G[u]]
    edges.sort()
    for W,u,v in edges:
        if subtrees[u] != subtrees[v]:
            tree.append((u,v))
            subtrees.union(u,v)
    return tree        



def inputToDict(filename):

<<<<<<< HEAD
    
    
    file = open(filename).readlines()

    dict = []
    maximum = 0
=======
    dict = {}
    
    file = open(filename).readlines()
>>>>>>> origin/Kruskal
    for line in file:
        split = line.split(" ")
        if len(split) > 1:
            if '\n' in split[2]:
                split[2] = split[2][:-1]
<<<<<<< HEAD
            #print "'{0}', '{1}', '{2}', '{3}'".format("line", split[0], split[1], split[2])    
            dict.append([split[0],split[1],split[2]])
            if split[0] > maximum: maximum = int(split[0])
            if split[1] > maximum: maximum = int(split[1])
            #dict[split[0]][split[1]] = 2
            #dict[split[1]][[split[0]] = 2
            #notSpan.append([split[0],split[1],split[2]])
        #else:
            #for i in range(0, int(split[0][:-1])):
            #    dict[str(i)] = {}
        
    #d_arr = {(x,y): for x in range(len(dict)) for y in range(len(dict))} 
    d_arr = {}
    for i in dict:
        if int(i[0]) in d_arr: 
            d_arr[int(i[0])][int(i[1])] = int(i[2])
        else:
            print "hallo"
            d_arr[int(i[0])] = {int(i[1]):int(i[2])}
        if int(i[1]) in d_arr: 
            d_arr[int(i[1])][int(i[0])] = int(i[2])
        else:
            d_arr[int(i[1])] = {int(i[0]):int(i[2])}
    return d_arr


g = inputToDict("simple.in")
x = MinimumSpanningTree(g)
print x
=======
                
            dict[split[0]][split[1]] = split[2]
            dict[split[1]][[split[0]] = split[2]
            notSpan.append([split[0],split[1],split[2]])
        else:
            for i in range(0, int(split[0][:-1])):
                dict[str(i)] = {}
    return dict


g = inputToDict("10.in")
#x = MinimumSpanningTree(g)
#print x
>>>>>>> origin/Kruskal
