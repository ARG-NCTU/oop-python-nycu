import numpy as np

class Mat:
    __data: np.ndarray

    def __init__(self,
                 mat: list = []):
        data = np.array(mat)
        assert len(data.shape) == 2 or mat == [], 'Warning: shape format wrong'
        self.__data = data

    """ Set matrix by the input matrix """
    def set(self, mat):
        data = np.array(mat)
        assert data.shape == self.shape(), 'Warning: input data shape wrong'
        self.__data = data

    """ Get shape of matrix """
    def shape(self)-> tuple:
        return self.__data.shape

    # operator overridings
    ########################################################################

    """ Matrix addition """
    def __add__(self, other):
        assert self.shape() == other.shape(), 'Error: matrix shape vary'
        return Mat(np.vectorize(lambda a, b: a + b)(self.__data, other.__data))

    """ Matrix subtract """
    def __sub__(self, other):
        assert self.shape() == other.shape(), 'Error: matrix shape vary'
        return Mat(np.vectorize(lambda a, b: a - b)(self.__data, other.__data))

    """ Matrix multiplication """
    def __mul__(self, other):
        assert self.__data.shape[1] == other.__data.shape[0], 'Warning: matrices shape not fit'

        data = []
        K = self.__data.shape[1]
        for i in range(self.__data.shape[0]):
            for j in range(other.__data.shape[1]):
                data[i].append(self.__data[i][0] * other.__data[0][j])
                for k in range(1, K):
                    data[i][j] += self.__data[i][k] * other.__data[k][j]
        return Mat(data)

    """ Get element """
    def __getitem__(self, key: tuple):
        return self.__data[key[0], key[1]]

    ########################################################################

    """ Get copy of matrix """
    def copy(self):
        return Mat(self.__data)
    
    def transpose(self):
        mat = np.zeros_like(self.__data, shape= (self.__data.shape[1], self.__data.shape[0]))
        for i in np.mgrid[0:self.__data.shape[1]]:
            for j in np.mgrid[0:self.__data.shape[0]]:
                mat[i][j] = self.__data[j][i]
        return Mat(mat)

    """ Print matrix """
    def print(self):
        print(self.__data)

m1 = Mat([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]])
m2 = Mat([[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]])
m3 = Mat()
m3.print()
m3 = m1 * m2

m3print()
print(0)