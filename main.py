from functions import * 

if __name__ == '__main__':
    draw_matrix = []

    I = [
        [1, 1],
        [1, 2],
        [1, 6],
        [1, 8],
        [1, 9],
        [2, 1],
    ]

    # converting Ind vectors into Class instances 
    classes_nb = len(I)
    for i in range(classes_nb):
        I[i] = Class(I[i], '{}'.format(i), weight = 1)
        
    # start CAH
    while len(I) > 1:
        s = calculate_distances_table(I, I)
        s.show()

        # get smallest distance and its cordinates in table s 
        r, y, x = s.get_smallest_val()

        # removing the classes where the smallest distance was found 
        if x > y:
            a, b = I.pop(x), I.pop(y)
        else:
            a, b = I.pop(y), I.pop(x)

        # save removed classes labels and distance between them for drawing later
        draw_matrix += [[int(a.label), int(b.label), r, 0]]

        # creating a new class that regroups the old removed classes
        new = Class(
            vect = [], 
            label = '{}'.format(classes_nb), 
            ro = r,
            group = [b,a],
        )

        classes_nb += 1

        # updating the I vector with the newly created class 
        I = [new, *I]

    # draw the dendrogram 
    draw(draw_matrix)