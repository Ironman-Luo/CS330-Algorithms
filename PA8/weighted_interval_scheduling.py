def function(Input, num):
    p = ['-'] * num
    M = [-1] * num
    reverse = [num - 1 - i for i in range(num)]
    Input = sorted(Input, key = lambda x: x[2])
    for i in reverse:
        
        j = i - 1
        while Input[j][2] > Input[i][1] and j >= 0:
            j = j - 1
        if j != -1:
            p[i] = j
        else:
            p[i] = '-'
    M[0] = Input[0][3]
    output = []
    for i in range(1 , num):
        if p[i] == '-':
            M[i] = max(Input[i][3], M[i - 1])
        else:
            M[i] = max(Input[i][3] + M[p[i]], M[i - 1])
    x = M[-1]
    i = num - 1
    while x > 0:
        while M[i] == M[i - 1]:
            i = i - 1
        output += [Input[i][0]]
        x = x - Input[i][3]
        i = p[i]
    return output

def main():
    f = open("input", "r")
    file = f.readlines()
    Input = []
    for i in file[1:]:
        if i[-1] == "\n":
            i = i[:-1]
        newi = i.split(",")
        for i in range(len(newi)):
            newi[i] = int(newi[i])
        if newi[1] < newi[2]:
            Input +=[newi]
    num_of_intervals = len(Input)
    output = function(Input,num_of_intervals)
    f1 = open("output", "w")
    for i in range(len(output)):
        f1.write(str(output[i]))
        f1.write("\n")
    f1.close()
    

            
if __name__ == "__main__":
    main()
