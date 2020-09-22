file1 = open("pref_file_1","r+")
file2 = open("pref_file_2","r+")
File1 = file1.readlines()
File2 = file2.readlines()
num = int(File1[0])
freeMan = list(range(0, num))
manNext = [0] * num
womenMatch = [-1] * num
output = [None] * num
fileOutput = open("output","w+")

def turnToList(S):
    S = S.replace('\n','')
    S = S.split(',')
    return S

def reverseOrder(L):
    index = 0
    finalList = []
    for i in L:
        curlist = [None] * num
        for index, ele in list(enumerate(i)):
            curlist[int(ele)] = index
        finalList.append(curlist)
    return finalList

fmen = []
for i in File1[1:]:
    a = [turnToList(i)]
    fmen += a
fmen = reverseOrder(fmen)

fwomen = []
for i in File2[1:]:
    a = [turnToList(i)]
    fwomen += a

while freeMan != []:
    m = freeMan.pop()
    w = fmen[m][manNext[m]]

    if womenMatch[w] == -1:
        output[m] = [m, w]
        manNext[m] += 1
        womenMatch[w] = m

    elif int(fwomen[w][womenMatch[w]]) >= int(fwomen[w][m]):
        output[womenMatch[w]] = None
        freeMan.append(womenMatch[w])
        womenMatch[w] = m
        output[m] = [m, w]
        manNext[m] += 1

    else:
        manNext[m] += 1
        freeMan.append(m)

for element in output:
    fileOutput.write(str(element[0]))
    fileOutput.write(",")
    fileOutput.write(str(element[1]))
    fileOutput.write('\n')
fileOutput.close()






