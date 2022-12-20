import data
import numpy as np
import math

path = "./data/graph_6.txt"

def HITS(adj_mat,n,e):
    adj_mat = np.array(adj_mat)
    last_aut = np.ones(n)
    last_hub = np.ones(n)
    aut = np.ones(n)
    hub = np.ones(n)
    eps = 0.001
    t = 1
    while True:

        for i in range(n):
            aut[i] = np.sum(adj_mat.transpose()[i]*last_hub)
            hub[i] = np.sum(adj_mat[i]*last_aut)
          
        #Normalization
        aut = aut/np.sum(aut)
        hub = hub/np.sum(hub)
        if np.linalg.norm(aut-last_aut) + np.linalg.norm(hub-last_hub)<eps:
            break
        else:
            last_aut = aut.copy()
            last_hub = hub.copy()
    return aut,hub



if __name__ == "__main__":
    n,e = data.get_n_e(path)
    data = data.get_amat(path)
    print(data)
    aut,hub = HITS(data,n,e)
    print(aut)
    print(hub)
    