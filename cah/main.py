from functions import * 

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
        I[i] = Class(I[i], '{}'.format(i + 1), weight = 1)
        

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
            label = '{}'.format(classes_nb), 
            ro = r,
            group = [b,a],
        )

        classes_nb += 1

        I = [new, *I]

    data = get_draw_data(I[0])

    ## drawing 
    root_nb = list(data.keys())[0]
    root = Node(int(root_nb))
    createTree(root, data[root_nb][0], True)
    createTree(root, data[root_nb][1], False)
    print(root)

    ## more info
    more_data = get_draw_data_2(I[0])
    print (json.dumps(more_data, sort_keys=False, indent=3))

    
