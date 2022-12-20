import data
import numpy as np
import networkx as nx

path = './data/graph_1.txt'

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
        pr = pr/np.sum(pr)
        if np.linalg.norm(pr-last_pr) < eps:
            break
        else:
            last_pr = pr.copy()
    return pr   

if __name__ == "__main__":
    G = data.get_graph(path)
    pr = pagerank(G)
    print(pr)