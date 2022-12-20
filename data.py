import config
path = "./data/graph_1.txt"

def read_files(path):
    with open (path, "r") as myfile:
        data = myfile.read().splitlines()
    for i in range(len(data)):
        data[i] = data[i].split(",")
        data[i][0] = int(data[i][0])
        data[i][1] = int(data[i][1])
    return data

def gen_graph(data):
    print(config.g_info)
    return

if __name__=="__main__":
    data = read_files(path)
    print(data)
    gen_graph(data)