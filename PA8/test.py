f1 = open("output_2.txt", "r")
f2 = open("output","r")
file = f1.readlines()
file2 = f2.readlines()
input1 = []
for i in file:
    if i[-1] == "\n":
        i = i[:-1]
    input1 += [int(i)]


input2 = []
for i in file2:
    if i[-1] == "\n":
        i = i[:-1]
    input2 += [int(i)]
for i in range(len(input1)):
    if input1[i] != input2[i]:
        print(input1[i])


f = open("input", "r")
file = f.readlines()
Input = []
for i in file[1:]:
    if i[-1] == "\n":
        i = i[:-1]
        newi = i.split(",")
        for i in range(len(newi)):
            newi[i] = int(newi[i])
        Input +=[newi]
result = 0
result2 = 0
for i in input1:
    result += Input[i][3]
for i in input2:
    result2 += Input[i][3]
print(result, result2)
