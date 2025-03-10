import numpy as np

class Mat:
    __data: np.ndarray

    def __init__(self,
                 mat: list[list] = None):
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
        M = self.copy()
        M += other
        return M
    
    """ Matrix subtract """
    def __sub__(self, other):
        M = self.copy()
        M -= other
        return M
    
    """ Matrix multiplication """
    def __mul__(self, other):
        assert self.__data.shape[1] == other.__data.shape[0], 'Warning: matrices shape not fit'
        k = self.__data.shape[1]
        M = np.vectorize()(self.__data, other.__data)
        return 
    
    """ Get element """
    def __getitem__(self, key: tuple):
        return self.__data[key[0], key[1]]
    
    ########################################################################
    
    """ Get copy of matrix """
    def copy(self):
        return Mat(self.__data)
    
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
m3 = m1 + m2
print(m3[1, 2])

m3.print()
print(0)