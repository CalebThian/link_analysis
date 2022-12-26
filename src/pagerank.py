import data
import numpy as np
import networkx as nx
from utils import timer

path = './data/graph_6.txt'

@timer
def pagerank(G,d=0.1):
    n = len(G.nodes)
    index = data.construct_index(G.nodes)
    
    last_pr = np.ones(n)/n
    pr = last_pr.copy()
    outdegree = np.ones(n)
    for node in list(G.nodes):
        outdegree[index[node]] = len(list(G.successors(node)))
    eps = 0.001
    
    while True:
        for node in list(G.nodes):
            par = list(G.predecessors(node))
            pr_in = 0
            if len(par) != 0:
                for p in par:
                    pr_in += last_pr[index[p]]/outdegree[index[p]]
            pr[index[node]] = d/n+(1-d)*pr_in
        
        if np.linalg.norm(pr-last_pr) < eps:
            break
        else:
            last_pr = pr.copy()
    return pr/np.sum(pr)

def output_file(pr,path):
    outdir = "../results/"
    file = path.split('/')[-1]
    file = outdir+file[:-4]+"/"+file
    file = file[:-4]+"_PageRank.txt"
    np.savetxt(file, pr, fmt='%.3f', delimiter="",newline=' ')

if __name__ == "__main__":
    G = data.get_graph(path)
    pr = pagerank(G)
    print(pr)
    output_file(pr,path)