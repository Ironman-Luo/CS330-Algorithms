import math


def Recursive_Multiply(firstnum, secondnum):
    if len(firstnum) <= 5 and len(secondnum) <= 5:
        return grade_school(firstnum,secondnum)
    if len(firstnum) > len(secondnum):
        secondnum = add_zero(secondnum, len(firstnum) - len(secondnum))
    elif len(firstnum) < len(secondnum):
        firstnum = add_zero(firstnum, len(secondnum) - len(firstnum))    
    half = len(firstnum)//2
    if (len(firstnum) % 2) != 0:
        half += 1
    B = len(firstnum) - half
    A = B * 2
    x1 = firstnum[:half]
    x0 = firstnum[half:]
    y1 = secondnum[:half]
    y0 = secondnum[half:]
    a = ab(x1,x0)
    b = ab(y1, y0)
    p = Recursive_Multiply(a, b)
    c = Recursive_Multiply(x1, y1)
    d = Recursive_Multiply(x0, y0)
    A1 = add_zero(c, A, False)
    B1 = add_zero((sb(sb(p, c), d)), B, False)
    return ab(ab(A1,B1),d)

def add_zero(string, number, left = True):
    for i in range(number):
        if left:
            string = '0' + string
        else:
            string += '0'
    return string


def grade_school(firstnum,secondnum):
    if len(firstnum) > len(secondnum):
        m = secondnum
        n = firstnum
    else:
        m = firstnum
        n = secondnum
    result = '0'
    length = len(m) - 1
    i = len(m) - 1
    while i >= 0:
        if m[i] == '1':
            temp = add_zero(n,length - i,False)
            result = ab(result, temp)
        i = i - 1
    return result
            
    

def ab(b1, b2):
    if len(b1) > len(b2):
        b2 = add_zero(b2,len(b1)-len(b2))
    elif len(b2) > len(b1):
        b1 = add_zero(b1, len(b2) - len(b1))
    i = len(b1) - 1
    result = ''
    carry = 0
    while i >= 0:
        x = int(b1[i])
        y = int(b2[i])
        add = x ^ y ^ carry
        result = str(add) + result
        if (x == 0 and y == 1 and carry == 1) or (x == 1 and y == 0 and carry == 1) or (x == 1 and y == 1 and carry == 0):
            carry = 1
        elif x & y & carry:
            carry = 1
        else:
            carry = 0
        i = i - 1
    if carry == 1:
        result = '1' + result
    return result
        

def sb(b1, b2):
    if len(b1) > len(b2):
        b2= '0' * (len(b1)-len(b2)) + b2
    if len(b1) < len(b2):
        b1 = '0' * (len(b2)-len(b1)) + b1
    i = len(b1) -1
    result = ''
    borrow = 0
    while i >=0:
        x = int(b1[i])
        y = int(b2[i])
        subtraction = x ^ y ^ borrow
        result = str(subtraction) + result
        if x == 0 and (y == 1 or borrow == 1):
            borrow = 1
        elif x & y & borrow:
            borrow = 1
        else:
            borrow = 0
        i = i - 1
    return result
            
def main():
    f = open("04_input", "r")
    file = f.readlines()
    num_of_bits = int(file[0])
    firstnum = str(file[1][:-1])
    secondnum = str(file[2][:-1])
    print(grade_school(firstnum,secondnum))
    f = open("output", "w")
    f.write(Recursive_Multiply(firstnum, secondnum))
    f.close()
    
    

if __name__ == "__main__":
    main()
