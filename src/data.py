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
    if "ibm" not in path:
        for i in range(len(data)):
            data[i] = data[i].split(",")
            data[i][0] = int(data[i][0])
            data[i][1] = int(data[i][1])
    else:
        for i in range(len(data)):
            data[i] = data[i].split()
            #print(data[i])
            data[i] = [int(data[i][1]),int(data[i][2])]
    return data

def gen_graph(data):
    graph = nx.DiGraph()
    graph.add_edges_from(data)
    return graph

def get_graph(path):
    data = read_file(path)
    graph = gen_graph(data)
    return graph

def draw_graph(path):
    data = read_file(path)
    graph = gen_graph(data)
    nx.draw(graph,with_labels=True)
    
if __name__=="__main__":
    data_path = "./data/"
    file = "ibm-5000.txt"
    data = read_file(data_path+file)
    G = gen_graph(data)
    print(len(list(G.nodes)))