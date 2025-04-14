import numpy as np

class Mat:
    __data: np.ndarray

    def __init__(self,
                 mat: list = None):
        data = np.array(mat)
        assert len(data.shape) == 2 or mat == None, 'Warning: shape format wrong'
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
        return Mat(np.matmul(self.__data, other.__data))

    """ Get element """
    def __getitem__(self, key: tuple):
        assert len(key) == 2, 'Error: key values invalid'
        assert key[:1] < self.__data.shape[:1], 'Error: key value overflow'
        return self.__data[key]

    """ To string """
    def __str__(self):
        return self.__data.__str__()

    ########################################################################

    """ Get copy of matrix """
    def copy(self):
        return Mat(self.__data)
    
    """ Get transpose of matrix """
    def transpose(self):
        return Mat(self.__data.transpose())

    """ Print matrix """
    def print(self):
        print(self.__data)

# # Test
# m1 = Mat([[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]])
# m2 = Mat([[1, 1, 1],
#           [1, 1, 1],
#           [1, 1, 1]])
# m3 = Mat()
# m3.print()
# m3 = m1 * m2
# m3.transpose().print()
# m3.set([[1, 2, 3],
#         [4, 5, 6]])
# m3.print()

# print(0)