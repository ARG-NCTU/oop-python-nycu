import numpy as np

class Mat:
    __data: np.ndarray    # 

    def __init__(self,
                 mat: list[list] = []):
        data = np.array(mat)
        assert len(data.shape) == 2, 'Warning: shape format wrong'
        self.__data = data
    
    def set(self, mat):
        data = np.array(mat)
        assert data.shape == self.shape(), 'Warning: input data shape wrong'
        self.__data = data

    """ Get shape of matrix """
    def shape(self)-> tuple:
        return self.__data.shape
    
    """ Matrix  """
    def __iadd__(self, other):
        assert self.shape() == other.shape(), 'Warning: shape of matrices vary'
        self.__data = np.vectorize(lambda a, b: a + b)(self.__data, other.__data)
        return self
    
    """ Matrix addition """
    def __add__(self, other):
        M = self.copy()
        M += other
        return M
    
    def copy(self):
        return Mat(self.shape(), self.__data)

m1 = Mat([[1, 2, 3]])
m2 = Mat([[1, 1, 1]])
m3 = Mat()
m3 = m1 + m2

print(m1.shape())
print(0)