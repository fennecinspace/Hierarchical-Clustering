
# External - for ploting
from scipy.cluster.hierarchy import dendrogram
from matplotlib import pyplot as plt 
import numpy as np  # to create dendrogram matrix

# Mine
from matrix import Table, Class


def calculate_distances_table(D, M):
    # create a table of width M and height D
    s = Table(len(M), len(D), labelsX=[e.label for e in M], labelsY = [e.label for e in D])
    
    # fill the table
    for i in range(len(D)):
        for j in range(len(M)):
            # if i == j => class is the same, which means distance = 0
            if i != j:
                if D[i].group[0] == D[i] and M[j].group[0] == M[j]:
                    # both classes are individuals
                    s.matrix[i][j] = calc_initial_ro(D[i], M[j])
                else: # one or both classes are composed of individuals
                    s.matrix[i][j] = calc_recurrence_ro(D[i], M[j])
            else:
                s.matrix[i][j] = 0

    return s


def calc_initial_ro(i, j):
    tmp = (i.weight * j.weight) /  (i.weight + j.weight)
    n = i.sub(j) # substract vector j from i
    dist = sum([e**2 for e in n.vector])
    return tmp * dist


def calc_recurrence_ro(i, j):
    weights_sum = i.weight + j.weight
    
    if len(j.group) != 2: # if i is composed class and j is individual ... swap them
        t = i
        i = j
        j = t
    
    if i.vector and j.vector:
        return calc_initial_ro(i,j)

    # sum of (weights * distances) of i, first component of j and second component of j
    cl_ro = - (i.weight * i.ro) - (j.group[0].weight * j.group[0].ro) - (j.group[1].weight * j.group[1].ro)

    # distance between i (ind) and first component (ind) of j (class)
    ro1 = (i.weight + j.group[0].weight) * calc_recurrence_ro(i, j.group[0])
    
    # distance between i (ind) and second component (ind) of j (class)
    ro2 = (i.weight + j.group[1].weight) * calc_recurrence_ro(i, j.group[1])
    
    # distance between first component (ind) of j (class) and second component (ind) of j (class)
    ro3 = (j.group[0].weight + j.group[1].weight) * calc_recurrence_ro(j.group[0], j.group[1]) 

    return ( ro1 + ro2 + ro3 + cl_ro ) / weights_sum



def draw(linkage_matrix):
    fig = plt.figure(figsize=(5, 5))
    dn = dendrogram(linkage_matrix)
    plt.show()
