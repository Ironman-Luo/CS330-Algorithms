import copy
def main():
    (Input,n,m,s,t) = read_file("input")
    output = ford_fulkerson(Input,n,m,s,t)
    write_file(output)
def read_file(name):
    f = open(name , "r")
    file = f.readlines()
    num_of_nodes = int(file[0])
    num_of_edges = int(file[1])
    startnode = int(file[2])
    endnode = int(file[3])
    Input = []
    for i in file[4:]:
        
        if i[-1] == "\n":
            i = i[:-1]    
        newi = i.split(",")
        for i in range(len(newi)):
            newi[i] = int(newi[i])
        Input += [newi]
        
    return (Input,num_of_nodes,num_of_edges,startnode,endnode)

def ford_fulkerson(Input,n,m,s,t):
    adj = generate_adj(Input, n)
    print(adj)
    lw = copy.deepcopy(adj)
    f = [0] * len(Input)
    parent = [-1] * len(adj)
    max_flow = 0
    while BFS(adj,s,t,parent)[0]:
        print(parent)

        path_flow = float("inf")
        current = t
        while current != s:
        
            for i in adj[parent[current]]:
                if i[0] == current:
                    path_flow = min(path_flow, i[1])
                    break
            current = parent[current]
        max_flow +=  path_flow
        v = t
        while v != s:
            u = parent[v]
            index = 0
            for x in adj[v]:
                if x[0] == u:
                    x[1] += path_flow
                    break
                index += 1
            if index == len(adj[v]):
                adj[v] += [[u,path_flow]]
            for x in adj[u]:
                if x[0] == v:
                    x[1] -= path_flow
                    break
            v = parent[v]
    for i in range(len(lw)):
        for j in range(len(lw[i])):
            lw[i][j][1] -= adj[i][j][1]
    return lw


def BFS(adj,s,t,parent):
    visited =[False] * len(adj)
    queue=[]
    queue.append(s) 
    visited[s] = True
    while queue:
        print(queue)
        u = queue.pop(0)
        for [i, val] in adj[u]:
            if visited[i] == False and val > 0 : 
                queue.append(i) 
                visited[i] = True
                parent[i] = u
    return (visited[t], parent)



def generate_adj(Input,n):
    adj = [[] for i in range(n)]
    for i in Input:
        adj[i[0]] += [[i[1], i[2]]]

    return adj

def write_file(output):
    f = open("output","w")
    for i in range(len(output)):
        if len(output[i]) != 0:
            for j in range(len(output[i])):
                if output[i][j] != []:
                    f.write(str(i))
                    f.write(",")
                    f.write(str(output[i][j][0]))
                    f.write(",")
                    f.write(str(output[i][j][1]))
                    f.write("\n")
    f.close()


if __name__ == "__main__":
    main()
    
