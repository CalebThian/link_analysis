from config import g_info
import numpy as np

def read_files(path):
    with open (path, "r") as myfile:
        data = myfile.read().splitlines()
    for i in range(len(data)):
        data[i] = data[i].split(",")
        data[i][0] = int(data[i][0])
        data[i][1] = int(data[i][1])
    return data

def gen_graph(data,n,e):
    adj_mat = np.zeros((n,n))
    for d in data:
        adj_mat[d[0]-1][d[1]-1] = 1
    return adj_mat

def get_amat(path):
    file = path.split('/')[-1]
    n,e = g_info[file][0],g_info[file][1]
    data = read_files(path)
    adj_mat = gen_graph(data,n,e)
    return adj_mat

if __name__=="__main__":
    data_path = "./data/"
    file = "graph_1.txt"
    
    n,e = g_info[file][0],g_info[file][1]
    data = read_files(data_path+file)
    adj_mat = gen_graph(data,n,e)