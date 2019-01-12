
import json
from binarytree import tree, Node
from matrix import Table, Class

def calculate_distances_table(D, M, old_Table = None):
    s = Table(len(M), len(D), labelsX=[e.label for e in M], labelsY = [e.label for e in D])
    
    for i in range(len(D)):
        for j in range(len(M)):
            if i != j:
                if D[i].group[0] == D[i] and M[j].group[0] == M[j]:
                    s.matrix[i][j] = calc_initial_ro(D[i], M[j])
                else:
                    s.matrix[i][j] = calc_recurrence_ro(D[i], M[j])
            else:
                s.matrix[i][j] = 0

    return s


def calc_initial_ro(i, j):
    tmp = (i.weight * j.weight) /  (i.weight + j.weight)
    n = i.sub(j)
    dist = sum([e**2 for e in n.vector])
    return tmp * dist


def calc_recurrence_ro(i, j):
    weights_sum = i.weight + j.weight
    
    if len(j.group) != 2:
        t = i
        i = j
        j = t
    
    if i.vector and j.vector:
        return calc_initial_ro(i,j)

    cl_ro = - (i.weight * i.ro) - (j.group[0].weight * j.group[0].ro) - (j.group[1].weight * j.group[1].ro)

    ro1 = (i.weight + j.group[0].weight) * calc_recurrence_ro(i, j.group[0])
    ro2 = (i.weight + j.group[1].weight) * calc_recurrence_ro(i, j.group[1])
    ro3 = (j.group[0].weight + j.group[1].weight) * calc_recurrence_ro(j.group[0], j.group[1]) 

    return ( ro1 + ro2 + ro3 + cl_ro ) / weights_sum


def get_draw_data_2(c):
    if not c.vector:
        return [{
            'label' : c.label,
            'ro': round(c.ro,2),
            'content': get_draw_data_2(c.group[0]) + get_draw_data_2(c.group[1])
        }]
    else:
        return [{
            'label': c.label,
        }] 

def get_draw_data(c):
    if not c.vector:
        return {
            c.label : [get_draw_data(c.group[0]) , get_draw_data(c.group[1])]
        }
    else:
        return c.label


def createTree(root, data, right):
    if type(data).__name__ == 'dict':
        root_nb = list(data.keys())[0]
        if right:
            root.right = Node(int(root_nb))
            createTree(root.right, data[root_nb][1], True)
            createTree(root.right, data[root_nb][0], False)
        else:
            root.left = Node(int(root_nb))
            createTree(root.left, data[root_nb][1], True)
            createTree(root.left, data[root_nb][0], False)
    else:
        if right:
            root.right = Node(int(data[0]))
        else:
            root.left = Node(int(data[0]))
