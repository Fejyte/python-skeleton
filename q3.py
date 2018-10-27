# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
edgeList2 = []
def question03(numNodes, edgeList):
  edgeList2 = edgeList

class GraphNode(object):
    def __init__(self,key):
        self.key = key
        self.nb = []
        self.cn = []
    def __lt__(self,other):
        if len(self.nb) == len(other.nb):
            return len(self.cn) < len(other.cn)
        else:
            return len(self.nb) < len(other.nb)
            

    

def edgeadd(edge):
    w1 = edge["edgeA"]
    w2 = edge["edgeB"]
    v1 = GraphNode(w1) 
    v2 = GraphNode(w2)
    if w1 in nbl:
        nbl[w1].nb.append(w2)
    else:
        nbl[w1] = v1
        nbl[w1].nb = [w2]
    if w2 in nbl:
        nbl[w2].nb.append(w1)
    else:
        nbl[w2] = v2
        nbl[w2].nb = [w1]
        

for i in edgelist2:
    edgeadd(i)

for i in nbl:
    for j in nbl[i].nb:
        if len(nbl[j].nb) == len(nbl[i].nb):
           nbl[i].cn.append(nbl[j].key)
           
nbk = [k for k in sorted(nbl, key=lambda k:nbl[k])]
te = []
nte = []
cache = []
for x in nbk:
    relate = False
    for i in nbl[x].nb:
        if i in te:
            relate = True
            nte.append(x)
            break
    if not relate:
        te.append(x)

print (abs(len(nte)-len(te)))
