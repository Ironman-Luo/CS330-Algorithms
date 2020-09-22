f = open("input" , "r")
file = f.readlines()
num_of_intervals = int(file[0])
Input = []
k = 0
for i in file[1:]:
    
    if i[-1] == "\n":
        i = i[:-1]
        newi = i.split(",")
    else:
        newi = i.split(",")
    for i in range(len(newi)):
        newi[i] = int(newi[i])
        
    Input += [newi + [k]]
    k = k + 1

Input.sort(key=lambda x:x[1])
output = [Input[0][2]]
i = 0
while i < len(Input):
    finishtime = Input[i][1]
    while i < len(Input):
        if Input[i][0] > finishtime:
            output += [Input[i][2]]
            break
        i = i + 1
f2 = open("output", "w")
for x in output:
    f2.write(str(x))
    f2.write("\n")
f2.close()
