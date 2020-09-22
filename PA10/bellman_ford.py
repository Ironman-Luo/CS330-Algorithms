def main():
    (Input,n,m,s) = read_file("input")
    output = bellman_ford(Input,n,m,s)
    write_file("output",output)
def read_file(name):
    f = open(name , "r")
    file = f.readlines()
    num_of_nodes = int(file[0])
    num_of_edges = int(file[1])
    startnode = int(file[2])
    Input = []
    for i in file[3:]:
        
        if i[-1] == "\n":
            i = i[:-1]    
        newi = i.split(",")
        for i in range(len(newi)):
            newi[i] = int(newi[i])
        Input += [newi]
        
    return (Input,num_of_nodes,num_of_edges,startnode)

def write_file(name, file):
    f = open(name, "w")
    for i in file:
        f.write(str(i))
        f.write("\n")
    f.close()
def bellman_ford(Input, n,m,s):
    distance = [float("inf")] * n
    distance[s] = 0
    for k in range(n):
        for i in Input:
            if distance[i[0]] != float("inf") and\
               distance[i[0]] + i[2] < distance[i[1]]:
                distance[i[1]] = distance[i[0]] + i[2]
    return distance
if __name__ == "__main__":
    main()
    
