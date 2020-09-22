from numpy.random import random
import math

def generate_graph_uniform(n):
    f1 = open("input.txt", "w")
    f1.write(str(n) +"\n")
    f1.write(str(0) +"\n")
    for x in range(n):
        for y in range(x + 1, n):
            weight = random()
            f1.write('{0},{1},{2}\n'.format(x,y,weight))
    f1.close()

def generate_graph_heavier(n):
    f1 = open("input.txt", "w")
    f1.write(str(n) +"\n")
    f1.write(str(0) +"\n")
    for x in range(n):
        for y in range(x + 1, n):
            weight = random() ** (1/3)
            f1.write('{0},{1},{2}\n'.format(x,y,weight))
    f1.close()
def generate_graph_euclidean(n):
    f1 = open("input.txt", "w")
    f1.write(str(n) +"\n")
    f1.write(str(0) +"\n")
    vertex = [[random(),random()] for i in range(n)]
    for x in range(n):
        for y in range(x + 1, n):
            weight = ((vertex[x][0] - vertex[y][0]) ** 2 + (vertex[x][1] - vertex[y][1]) ** 2) ** (1/2)
            f1.write('{0},{1},{2}\n'.format(x,y,weight))
    f1.close()
