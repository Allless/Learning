class Matrix:
    def __init__(self, *args, **kwargs):
        """
        Takes 2 keyword arguments: filename or list. If filename is given
        read the matrix from file. Else, read it directly from list.
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            matrix_list = f.readlines()
        matrix_list = list(map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list))
        self.read_as_list(matrix_list)

    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'colums = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s

    def write_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                result = '\n'.join([' '.join(map(str, row)) for row in self._matrix])
                file.write(result)
        except:
            raise FileNotFoundError('Error while working with file')
    
    def transpose(self):
        self._matrix = [[col[j] for col in self._matrix ]for j in range(len(self._matrix))]

    @property
    def shape(self):
        return self._columns, self._rows

    def __add__(self, other):
        if type(other) != Matrix:
            raise TypeError('Matrix excepted')
        if self.shape != other.shape:
            raise ValueError('Matrixes have different sizes')
        newList = [[self._matrix[i][j] + other._matrix[i][j] for j in range(len(self._matrix[i]))] for i in range(len(self._matrix))]
        return Matrix(list = newList)

    def __mul__(self, other):
        if type(other) not in (int,float,Matrix):
            raise TypeError('Matrix or number excepted')
        if type(other) in (int,float):
            newList = [self._matrix[i][j] * other for i in range(len(self._matrix)) for j in range(len(self._matrix[i]))]
        else:
            newList = [[self._matrix[i][j] * other._matrix[i][j] for j in range(len(self._matrix[i]))] for i in range(len(self._matrix))]
        return Matrix(list = newList)

    def __matmul__(self, other):
        if type(other) != Matrix:
            raise TypeError('Matrix excepted')
        if len(self._matrix[0]) != len (other._matrix):
            raise ValueError('Wrong Sizes for Matrixes')
        newList = [[sum([self._matrix[i][k] * other._matrix[k][j] for k in range(len(other._matrix))])   for j in range(len(other._matrix[0]))] for i in range(len(self._matrix))]
        return Matrix(list = newList)

    @property
    def trace(self):
        if len(self._matrix) != len(self._matrix[0]):
            raise ValueError('Square Matrix excepted')
        return sum([self._matrix[i][i] for i in range(len(self._matrix))])

    @property
    def determinant(self):
        if len(self._matrix) != len(self._matrix[0]):
            raise ValueError('Square Matrix excepted')
        if(len(self._matrix) == 1):
            return self._matrix[0][0]
        else:
            sum = 0
            for i in range(len(self._matrix)):
                minor = Matrix(list = [[col[l] for l in range(len(col)) if l != i] for col in self._matrix[1:]])
                sum += minor.determinant * self._matrix[0][i] * (-1)**(i)
            return sum

a = Matrix(list = [[5,0,1],[1,2,3],[3,3,2]])
b = Matrix(list = [[5,0,11],[1,2,5],[3,3,4]])
print(a.determinant, b.determinant)