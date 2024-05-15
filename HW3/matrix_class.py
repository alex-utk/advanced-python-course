from mixins import ShapeCheckMixin, PrintMixin, SubstractionMixin, \
                   DivisionMixin, PropertyMixin, SaveMixin


class CustomMatrix(ShapeCheckMixin):
    """
    Кастомный тип матриц. Для проверки размерности использую mixin с декоратором.
    """
    def __init__(self, matrix) -> None:
        # для удобства сделаем матрицу иммутабельной
        # соответственно размерность у нас тоже всегда одинаковая
        self._matrix = matrix
        self._shape = self._calc_shape__() 
    
    def _calc_shape__(self):
        return (len(self.matrix), len(self.matrix[0]))
    
    def _get_matrix_col(self, j):
        return [row[j] for row in self.matrix]

    @ShapeCheckMixin._shape_check(transposed=False)
    def __add__(self, other: 'CustomMatrix'): # +
        new_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            new_row = [elem_a + elem_b for elem_a, elem_b in zip(row_a, row_b)]
            new_matrix.append(new_row)
        return self.__class__(new_matrix)
        
    @ShapeCheckMixin._shape_check(transposed=False)
    def __mul__(self, other):  # *
        new_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            new_row = [elem_a * elem_b for elem_a, elem_b in zip(row_a, row_b)]
            new_matrix.append(new_row)
        return self.__class__(new_matrix)
    
    @ShapeCheckMixin._shape_check(transposed=True)
    def __matmul__(self, other): # @
        n_rows = self.shape[0]
        new_matrix = []
        for i in range(n_rows):
            new_row = []
            for j in range(n_rows):
                row_a = self.matrix[i]
                col_b = other._get_matrix_col(j)
                new_row.append(sum([a*b for a, b in zip(row_a, col_b)]))
            new_matrix.append(new_row)
        return self.__class__(new_matrix)

# порядок наследования важен
class SuperCustomMatrix(CustomMatrix, PropertyMixin, SubstractionMixin, DivisionMixin, PrintMixin, SaveMixin):
    """
    Улучшенные матрицы для задания 3.2
    """
    pass
    
