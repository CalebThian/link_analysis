from config import g_info
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os

def get_files(data_dir):
    files = os.listdir(data_dir)
    return files

def construct_index(nodes):
    index = dict()
    t = 0
    for node in sorted(list(nodes)):
        index[node] = t
        t += 1
    return index

def read_file(path):
    with open (path, "r") as myfile:
        data = myfile.read().splitlines()
    for i in range(len(data)):
        data[i] = data[i].split(",")
        data[i][0] = int(data[i][0])
        data[i][1] = int(data[i][1])
    return data

def gen_amat(data,n,e):
    adj_mat = np.zeros((n,n))
    for d in data:
        adj_mat[d[0]-1][d[1]-1] = 1
    return adj_mat

def get_amat(path):
    n,e = get_n_e(path)
    data = read_file(path)
    adj_mat = gen_amat(data,n,e)
    return adj_mat

def get_n_e(path):
    file = path.split('/')[-1]
    n,e = g_info[file][0],g_info[file][1]
    return n,e

def gen_graph(data):
    graph = nx.DiGraph()
    graph.add_edges_from(data)
    return graph

def get_graph(path):
    data = read_file(path)
    graph = gen_graph(data)
    nx.draw(graph,with_labels=True)
    return graph

def draw_graph(path):
    data = read_file(path)
    graph = gen_graph(data)
    nx.draw(graph,with_labels=True)
    
if __name__=="__main__":
    data_path = "./data/"
    file = "graph_1.txt"
    
    n,e = g_info[file][0],g_info[file][1]
    data = read_file(data_path+file)
    adj_mat = gen_graph(data,n,e)