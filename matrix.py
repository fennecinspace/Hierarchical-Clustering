class Matrix:
    def __init__(self, mat):
        self.matrix = mat

    def trace(self):
        trace = 0
        if len(self.matrix) == len(self.matrix[0]):
            for i in range(len(self.matrix)):
                trace += self.matrix[i][i]
            return trace
        else:
            return None

    @classmethod
    def check_size(self, a,b):
        if len(a) != len(b):
            return False

        for i in range(len(a)):
            if len(a[i]) != len(b[i]):
                return False

        return True

    @classmethod
    def check_size_2(self, a, b):
        for i in range(len(a)):
            if len(a[i]) != len(b):
                return False

        return True


    def add(self, b):
        if self.check_size(self.matrix, b.matrix):
            c = []
            for i in range(len(self.matrix)):
                c += [[]]
                for j in range(len(self.matrix[i])):
                    c[i] += [self.matrix[i][j] + b.matrix[i][j]]
            
            return Matrix(c)
        else:
            return None


    def sub(self, b):
        if self.check_size(self.matrix, b.matrix):

            c = []
            for i in range(len(self.matrix)):
                c += [[]]
                for j in range(len(self.matrix[i])):
                    c[i] += [self.matrix[i][j] - b.matrix[i][j]]
            
            return Matrix(c)
        else:
            return None

    @classmethod
    def get_col(self, matrix, index):
        col = []
        for line in matrix.matrix:
            col += [line[index]]
        return col

    @classmethod
    def get_line(self, matrix, index):
        return matrix.matrix[index]

    def mul(self, b):
        if self.check_size_2(self.matrix, b.matrix):
            c = []
            for i in range(len(self.matrix)):
                c += [[]]
                for j in range(len(b.matrix[0])):
                    c[i] += [0]

            for i in range(len(c)):
                for j in range(len(c[i])):
                    c[i][j] = sum([m*n for m,n in zip(self.get_line(self, i), self.get_col(b, j))])

            return Matrix(c)
        else:
            return None

    def show(self):
        print()
        for l in self.matrix:
            print('| ', end = '')
            for c in l:
                print('{:6.2f} '.format( round(float(c), 3)), end = "")
            print('|')
        print()


    def transpose(self):
        c = []
        for i in range(len(self.matrix[0])): 
            c +=  [self.get_col(self, i)]

        return Matrix(c)

    
    def __call__(self, row = None, col = None):
        if row == None and col == None:
            return self

        elif row == None:
            return Vector(self.get_col(self, col))

        elif col == None:
            return Vector(self.get_line(self, row), transpose = True)
        else:
            return self.matrix[row][col]




class Vector(Matrix):
    def __init__(self, vect, transpose = False):
        self.transposed = transpose

        super().__init__(self.create_mat(vect, transpose))

    @classmethod
    def create_mat(self, vect, transpose):
        if transpose:
            mat = [vect]
        else:
            mat = []
            for elem in vect:
                mat += [[elem]]
        return mat

    @property
    def vector(self):
        if self.transposed:
            return self.matrix[0]
        else:
            return self.get_col(self, 0)

    @vector.setter
    def vector(self, value):
        self.matrix = self.create_mat(value, self.transposed)


    def __call__(self, elem = None):
        if elem == None:
            return self
        else:
            return self.vector[elem]

    def add(self, b):
        res = super().add(b)
        if res:
            if len(res.matrix) == 1:
                return res(0)
            else:
                return res(None, 0)
        else:
            return None



    def sub(self, b):
        res = super().sub(b)
        if res:
            if len(res.matrix) == 1:
                return res(0)
            else:
                return res(None, 0)
        else:
            return None


class Class(Vector):
    def __init__(self, vect, label, weight = None, ro = 0, group = None):
        super().__init__(vect)
        self.label = label
        self.group = group or [self]
        self.weight = weight or sum([e.weight for e in self.group])
        self.ro = ro

    

class Table():
    def __init__(self, sizeX, sizeY, labelsX = None, labelsY = None):
        self.matrix = []
        for i in range(sizeX):
            self.matrix += [[]]
            for _ in range(sizeY):
                self.matrix[i] += [0]

        self.labelsX = labelsX
        self.labelsY = labelsY

        if not self.labelsX:
            self.labelsX = []
            for i in range(sizeX):
                self.labelsX += ['j' + str(i)]

        if not self.labelsY:
            self.labelsY = []
            for i in range(sizeY):
                self.labelsY += ['i' + str(i)]

    def __call__(self, row = None, col = None):
        if row == None and col == None:
            return self.matrix, self.labelsY, self.labelsX

        else:
            return self.matrix[row][col], self.labelsY[row], self.labelsX[col]

    def show(self):
        print('/|'.rjust(len(self.labelsY[0]) + 4), end = '')
        print
        for i in range(len(self.labelsX)):
            print(('{}'.format(self.labelsX[i])).rjust(7), end = '')
        print()

        for i, l in enumerate(self.matrix):
            print(('{}| '.format(self.labelsY[i])).rjust(len(self.labelsY[0]) + 5), end = '')
            for c in l:
                print('{:6.2f} '.format( round(float(c), 3)), end = '')
            print('|')
        print()

    def get_smallest_val(self):
        s = self.matrix[0][1]
        x = 1
        y = 0
        for j in range(len(self.matrix[0])):
            for i in range(len(self.matrix)):
                if self.matrix[i][j] < s and self.matrix[i][j] != 0:
                    s = self.matrix[i][j]
                    x = j
                    y = i

        return s, y, x