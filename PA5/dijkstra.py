import heapq 
f = open("input" , "r")
file = f.readlines()
num_of_nodes = int(file[0])
num_of_edges = int(file[1])
startnode = int(file[2])
Input = []
for i in file[3:]:
    
    if i[-1] == "\n":
        i = i[:-1]
        newi = i.split(",")
        temp = newi[0]
        newi[0] = newi[2]
        newi[2] = temp
        temp = newi[1]
        newi[1] = newi[2]
        newi[2] = temp
    else:
        newi = i.split(",")
        temp = newi[0]
        newi[0] = newi[2]
        newi[2] = temp
        temp = newi[1]
        newi[1] = newi[2]
        newi[2] = temp
    for i in range(len(newi)):
        newi[i] = int(newi[i])
        
    Input += [newi]
    
Input2 = [ [] for i in range(num_of_nodes)]
for x in Input:
    Input2[x[1]] += [[x[0],x[1],x[2]]]

output = [[2147483647,0] for i in range(num_of_nodes)]
output[startnode] = [0, '-']
cut = [x for x in Input if x[1] == startnode]
heapq.heapify(cut)
collect = [False] * num_of_nodes
collect[startnode] = True

while collect != [True] * num_of_nodes:
    temp = heapq.heappop(cut)
    collect[temp[2]] = True

    if output[temp[2]][0] > temp[0]:
        output[temp[2]][0] = temp[0]
        output[temp[2]][1] = temp[1]
    for x in Input2[temp[2]]:
        if output[x[2]][0] > output[x[1]][0] + x[0]:
            output[x[2]][0] = output[x[1]][0] + x[0]
            output[x[2]][1] = x[1]
        Input2[temp[2]] = []
        heapq.heappush(cut, [output[x[1]][0] + x[0], x[1], x[2]])
f2 = open("output", "w")
for x in output:
    f2.write(str(x[0]))
    f2.write(",")
    f2.write(str(x[1]))
    f2.write("\n")
f2.close()

            
