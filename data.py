path = "./data/graph_1.txt"

if __name__=="__main__":
    with open (path, "r") as myfile:
        data = myfile.read().splitlines()
        print(data)