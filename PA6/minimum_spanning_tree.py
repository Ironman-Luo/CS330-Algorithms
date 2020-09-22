import heapq 
from random_graph import generate_graph_uniform
from random_graph import generate_graph_heavier
from random_graph import generate_graph_euclidean


import timeit

def MST(name):
    f = open(name , "r")
    file = f.readlines()
    num_of_nodes = int(file[0])
    num_of_edges = int(file[1])
    Input = []
    for i in file[2:]:
        
        if i[-1] == "\n":
            i = i[:-1]
            newi = i.split(",")
            temp = newi[2]
            newi = [temp] + newi[:-1]
        else:
            newi = i.split(",")
            temp = newi[2]
            newi = [temp] + newi[:-1]
        newi[0] = float(newi[0])
        newi[1] = int(newi[1])
        newi[2] = int(newi[2])
            
        Input += [newi]
    Input.sort()
    Array = [ i for i in range(num_of_nodes) ]
    output = [[] for i in range(num_of_nodes)]
    visited = [False] * num_of_nodes
    totalweight = 0
    for i in range(len(Input)):
        number1 = Input[i][1]
        number2 = Input[i][2]
        weight = Input[i][0]
        if visited[number1] == False and visited[number2] == False:
            Array[number2] = Array[number1]
            output[number2] += [number1]
            output[number1] += [number2]
            visited[number1] = True
            visited[number2] = True
            totalweight += weight
        elif visited[number1] == False and visited[number2] == True:
            Array[number1] = Array[number2]
            output[number2] += [number1]
            output[number1] += [number2]
            visited[number1] = True
            totalweight += weight
        elif visited[number1] == True and visited[number2] == False:
            Array[number2] = Array[number1]
            output[number2] += [number1]
            output[number1] += [number2]
            visited[number2] = True
            totalweight += weight
        else:
            temp1 = number1
            temp2 = number2
            count1 = 0
            count2 = 0
            while Array[temp1] != temp1:
                count1 += 1
                temp1 = Array[temp1]
            while Array[temp2] != temp2:
                count2 += 1
                temp2 = Array[temp2]
            if temp1 != temp2:
                output[number2] += [number1]
                output[number1] += [number2]
                totalweight += weight
                if count1 >= count2:
                    Array[temp2] = temp1
                else:
                    Array[temp1] = temp2
    return totalweight
    f2 = open("output", "w")
    for x in output:
        f2.write(str(x)[1:-1])
        f2.write("\n")
    f2.close()



def calculateweight1(n):
    totalweight = 0
    for i in range(10):
        generate_graph_uniform(n)
        totalweight += MST("input.txt")
    return totalweight/10

def calculateweight2(n):
    totalweight = 0
    for i in range(10):
        generate_graph_heavier(n)
        totalweight += MST("input.txt")

    return totalweight/10

def calculateweight3(n):
    totalweight = 0
    for i in range(10):
        generate_graph_euclidean(n)
        totalweight += MST("input.txt")
    return totalweight/10


def calculatemin1(n):
    for i in range(10):
        generate_graph_uniform(n)
        f = open("input.txt" , "r")
        file = f.readlines()
        num_of_nodes = int(file[0])
        num_of_edges = int(file[1])
        Input = []
        for i in file[2:]:
            
            if i[-1] == "\n":
                i = i[:-1]
                newi = i.split(",")
                
            else:
                newi = i.split(",")
            newi[0] = int(newi[0])
            newi[1] = int(newi[1])
            newi[2] = float(newi[2])
                
            Input += [newi]
        Array = [2147483647 for x in range(n)]
        for x in Input:
            if Array[x[0]] > x[2]:
                Array[x[0]] = x[2]
            if Array[x[1]] > x[2]:
                Array[x[1]] = x[2]
        return sum(Array)

def calculatemin2(n):
    for i in range(10):
        generate_graph_heavier(n)
        f = open("input.txt" , "r")
        file = f.readlines()
        num_of_nodes = int(file[0])
        num_of_edges = int(file[1])
        Input = []
        for i in file[2:]:
            
            if i[-1] == "\n":
                i = i[:-1]
                newi = i.split(",")
                
            else:
                newi = i.split(",")
            newi[0] = int(newi[0])
            newi[1] = int(newi[1])
            newi[2] = float(newi[2])
                
            Input += [newi]
        Array = [2147483647 for x in range(n)]
        for x in Input:
            if Array[x[0]] > x[2]:
                Array[x[0]] = x[2]
            if Array[x[1]] > x[2]:
                Array[x[1]] = x[2]
        return sum(Array)

def calculatemin3(n):
    for i in range(10):
        generate_graph_euclidean(n)
        f = open("input.txt" , "r")
        file = f.readlines()
        num_of_nodes = int(file[0])
        num_of_edges = int(file[1])
        Input = []
        for i in file[2:]:
            
            if i[-1] == "\n":
                i = i[:-1]
                newi = i.split(",")
                
            else:
                newi = i.split(",")
            newi[0] = int(newi[0])
            newi[1] = int(newi[1])
            newi[2] = float(newi[2])
                
            Input += [newi]
        Array = [2147483647 for x in range(n)]
        for x in Input:
            if Array[x[0]] > x[2]:
                Array[x[0]] = x[2]
            if Array[x[1]] > x[2]:
                Array[x[1]] = x[2]
        return sum(Array)
    
        
        
        
def main():
    timeset = [8192]
    output = []
    
    for i in timeset:
        time1 = calculatemin1(i)
        time2 = calculatemin2(i)
        time3 = calculatemin3(i)
        average = [time1,time2,time3]
        output +=[average]
        print(average)
    


    





    
if __name__ == "__main__":
    main()



