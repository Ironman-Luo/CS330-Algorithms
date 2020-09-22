f = open("input", "r")
file = f.readlines()
num_of_nodes = int(file[0])
list1 = []
for i in file[1:]:
    if i[-1] == "\n":
        i = i[:-1]
        newi = i.split(",")
    else:
        newi = i.split(",")
    for i in range(len(newi)):
        if newi[i] == "-":
            newi[i] = -1
        else:
            newi[i] = int(newi[i])
        
    list1 += [newi]
list2 = [0 for i in range(num_of_nodes)]

for i in list1:
    for y in i:
        if y != -1:
            list2[y] += 1
stack = []
list3 = [False] * num_of_nodes
def topologicalorder(stack, list2,list1, list3):
    a = 0
    temp = []
    for x in range(len(list2)):
        if list2[x] == 0 and list3[x] == False:
            a = 1
            stack.append(x)
            temp += [x]
            list3[x] = True
    for z in temp:
        for y in list1[z]:            
            if y >= 0:
                list2[y] -= 1
    if len(stack) < num_of_nodes:
        topologicalorder(stack,list2,list1,list3)   
    return stack


a = topologicalorder(stack,list2,list1,list3)
f1 = open("output" , "w")
for x in a:
    f1.write(str(x))
    f1.write("\n")
f1.close()
  



