import data
import numpy as np
import networkx as nx
from utils import timer
path = "./data/graph_5.txt"

@timer
def Simrank(G,C = 0.7,max_iter = 30):
    n = len(G.nodes)
    index = data.construct_index(G.nodes)
    
    simrank = np.identity(n)
    last_simrank = np.identity(n)

    for i in range(max_iter):
        print(i,end="\r")
        for node1 in sorted(list(G.nodes)):
            for node2 in sorted(list(G.nodes)):
                if node1 == node2:
                    simrank[index[node1]][index[node2]] = 1
                else:
                    pre1 = sorted(list(G.predecessors(node1)))
                    pre2 = sorted(list(G.predecessors(node2)))
                    if len(pre1) == 0 or len(pre2) == 0:
                        continue
                    t = 0
                    for x in pre1:
                        for y in pre2:
                            t += last_simrank.copy()[index[x]][index[y]]
                    simrank[index[node1]][index[node2]] = t*C/(len(pre1)*len(pre2))
        last_simrank = simrank.copy()
    return simrank

def output_file(sr,path):
    outdir = "../results/"
    file = path.split('/')[-1]
    file = outdir+file[:-4]+"/"+file
    file = file[:-4]+"_SimRank.txt"
    np.savetxt(file, sr, fmt='%.3f', delimiter=" ",newline="\n")

if __name__ == "__main__":
    G = data.get_graph(path)
    sr = Simrank(G)
    print(sr)
    output_file(sr,path)
