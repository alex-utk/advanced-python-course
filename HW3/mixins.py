import re

class PrintMixin:
    def __str__(self) -> str:
        return "\n".join([re.sub("[\[\],]","",str(row)) for row in self._matrix])
    
class SubstractionMixin:
    def __sub__(self, other):
        new_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            new_row = [elem_a - elem_b for elem_a, elem_b in zip(row_a, row_b)]
            new_matrix.append(new_row)
        return self.__class__(new_matrix)
    
class DivisionMixin:
    def __truediv__(self, other):
        new_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            new_row = [elem_a / elem_b for elem_a, elem_b in zip(row_a, row_b)]
            new_matrix.append(new_row)
        return self.__class__(new_matrix)
    
    def __floordiv__(self, other):
        new_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            new_row = [elem_a // elem_b for elem_a, elem_b in zip(row_a, row_b)]
            new_matrix.append(new_row)
        return self.__class__(new_matrix)
    
    def __mod__(self, other):
        new_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            new_row = [elem_a % elem_b for elem_a, elem_b in zip(row_a, row_b)]
            new_matrix.append(new_row)
        return self.__class__(new_matrix)
    
class PropertyMixin:
    @property
    def shape(self):
        return self._shape
    
    @shape.setter
    def shape(self, new_shape):
        if len(new_shape) !=2:
            raise ValueError(f'Incorrects shape {new_shape}')
        self._shape = new_shape
    
    @property
    def matrix(self):
        return self._matrix

    
    @matrix.setter
    def matrix(self, new_matrix):
        self._matrix = new_matrix
        self.shape = (len(new_matrix), len(new_matrix[0]))
        
    class 
    