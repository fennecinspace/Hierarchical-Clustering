def print_matrix(D):
    print()
    for l in D:
        for c in l:
            print('[{:6.2f}] '.format( round(float(c), 3)), end = "")
        print()
    print()


def print_vector(D):
    print()
    for i, c in enumerate(D):
        print('[{:6.2f}] '.format(float(c)), end = "")
    print()


def initialize_masse(I):
    return [1 for i in I]


def calculate_distances_table(D, M):
    distances = []
    for i in range(len(M)):
        distances += [[]]
        # for _ in range(0, i):
        #     distances[i] += [0]
        for j in range(i, len(M)):
            distances[i] += [calculate_distance(I[i], I[j], M[i], M[j])]
    
    mirror_diagonale(distances)

    return distances


def calculate_distance(a_f, b_f, a_m, b_m):
    return sum([ (a_f[i] - b_f[i])**2 for i in range(len(a_f)) ]) * ( (a_m * b_m) / (a_m + b_m) )


def mirror_diagonale(D):
    res = [[] for l in D[1:]]
    for i, l in enumerate(D):
        for j, c in enumerate(l[1:]):
            res[i + j] += [c]

    for i, l in enumerate(res):
        print( D[i + 1])
        D[i + 1] = l + D[i + 1]


def get_smallet_dist(D):
    d = 99999999
    d_i = -1
    d_j = -1
    nb_found = 0
    for i, l in enumerate(D):
        for j, c in enumerate(l):
            if i != j:
                if c < d:
                    d, d_i, d_j = c, i, j
                    nb_found = 1
                elif c == d:
                    nb_found += 1
    
    if nb_found > 1:
        d_i, d_j = get_best_smallet_distance(D, d)
    
    return d_i, d_j


def get_best_smallet_distance(D, d):
    for j in range(len(D[0])):
        for i in range(len(D)):
            if D[i][j] == d and i != j:
                return i, j



if __name__ == '__main__':
    ## data
    I = [
        [1, 1],
        [1, 2],
        [1, 6],
        [1, 8],
        [1, 9],
        [2, 1],
    ];

    ## masse
    M = initialize_masse(I)

    ## printing initial data
    print_matrix(I)
    print_vector(M)

    ## calculating rq
    D = calculate_distances_table(I, M)
    print_matrix(D)

    print(get_smallet_dist(D))
