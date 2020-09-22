import queue
f = open("input", "r")
file = f.readlines()
num_of_nodes = int(file[0])
start = int(file[1])
list1 = []
for i in file[2:]:
    if i[-1] == "\n":
        i = i[:-1]
        newi = i.split(",")
    else:
        newi = i.split(",")
    for i in range(len(newi)):
        newi[i] = int(newi[i])
    list1 += [newi]

output = []
L = queue.Queue(maxsize=num_of_nodes)
remain = [i for i in range(num_of_nodes)]

for x in list1[start]:
    L.put(x)
    remain[x] = -1
remain[start] = -1
while L.empty() == False:
    a = L.get()
    temp = []
    for k in list1[a]:
        
        if remain[k] != -1:
            L.put(k)
            temp += [k]
            
            remain[k] = -1
    list1[a] = temp

for x in range(len(list1)):
    for y in list1[x]:
        if x not in list1[y]:
            list1[y] = [x] + list1[y]

f3 = open("output","w")
for x in list1:
    f3.write(str(x)[1:-1] + "\n")
f3.close()
