import data
import numpy as np

path = "./data/graph_3.txt"

def HITS(G):
    n = len(G.nodes)
    last_aut = np.ones(n)
    last_hub = np.ones(n)
    aut = np.ones(n)
    hub = np.ones(n)
    eps = 0.001
    
    index = data.construct_index(G.nodes)
        
    while True:
        aut = np.zeros(n)
        hub = np.zeros(n)
        for node in G.nodes:
            par = list(G.predecessors(node))
            chi = list(G.successors(node))
            for p in par:
                aut[index[node]] += last_hub[index[p]]
            for c in chi:
                hub[index[node]] += last_aut[index[c]]
          
        #Normalization
        aut = aut/np.sum(aut)
        hub = hub/np.sum(hub)
        
        if np.linalg.norm(aut-last_aut) + np.linalg.norm(hub-last_hub)<eps:
            break
        else:
            last_aut = aut.copy()
            last_hub = hub.copy()
    return aut,hub

def output_file(aut,hub,path):
    outdir = "./results/"
    file = path.split('/')[-1]
    file = outdir+file[:-4]+"/"+file
    a_file = file[:-4]+"_HITS_authority.txt"
    h_file = file[:-4]+"_HITS_hub.txt"
    np.savetxt(a_file, aut, fmt='%3f', delimiter=" ",newline=' ')
    np.savetxt(h_file, aut, fmt='%3f', delimiter=" ",newline=' ')
    
if __name__ == "__main__":
    G = data.get_graph(path)
    aut,hub = HITS(G)
    print(aut)
    print(hub)
    output_file(aut,hub,path)
    