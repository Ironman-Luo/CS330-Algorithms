def main():
    f = open("07_input", "r")
    file = f.readlines()
    num_of_bits = int(file[0])
    s1 = str(file[1][:-1])
    s2 = str(file[2][:-1])
    output = lcs(s1,s2,len(s1),len(s2))
    f1 = open("output", "w")
    f1.write(str(output))
    f1.close()
    
def lcs(s1,s2,m,n):
    c = [[0 for x in range(n+1)] for x in range(m+1)]
    temp = ['']
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
                
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            temp[0] = s1[i - 1] + temp[0]
            i -= 1
            j -= 1
        elif c[i - 1][j] > c[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
                
    print(temp[0])
            
    return temp[0]

                
            
    


if __name__ == "__main__":
    main()
