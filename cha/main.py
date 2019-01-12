
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
    if len(j.group) != 2:
        t = i
        i = j
        j = t
    
    if i.vector and j.vector:
        return calc_initial_ro(i,j)

    weights_sum = i.weight + j.weight

    cl_ro = (i.weight * i.ro) - (j.group[0].weight * j.group[0].ro) - (j.group[1].weight * j.group[1].ro)

    ro1 = (i.weight + j.group[0].weight) * calc_recurrence_ro(i, j.group[0])
    ro2 = (i.weight + j.group[1].weight) * calc_recurrence_ro(i, j.group[1])
    ro3 = (j.group[0].weight + j.group[1].weight) * calc_recurrence_ro(j.group[0], j.group[1]) 

    return ( ro1 + ro2 + ro3 - cl_ro ) / weights_sum




if __name__ == '__main__':
    I = [
        [1, 1],
        [1, 2],
        [1, 6],
        [1, 8],
        [1, 9],
        [2, 1],
    ]

    classes_nb = len(I) + 1

    for i in range(len(I)):
        I[i] = Class(I[i], 'i{}'.format(i + 1), weight = 1)
        

    while len(I) > 1:
        s = calculate_distances_table(I, I)
        s.show()

        r, y, x = s.get_smallest_val()

        if x > y:
            a, b = I.pop(x), I.pop(y)
        else:
            a, b = I.pop(y), I.pop(x)

        new = Class(
            vect = [], 
            label = 'i{}'.format(classes_nb), 
            ro = r,
            group = [a,b],
        )

        classes_nb += 1

        I = [new, *I]
