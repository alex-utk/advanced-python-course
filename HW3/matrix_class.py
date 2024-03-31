import numpy as np
# операции сложения и умножения (матричного и покомпонентного)
# через перегрузку операторов +, *, @ (как в numpy).
# Вызывать исключения, если матрицы на входе некорректной размерности (ValueError)


class CustomMatrix():
    def __init__(self, matrix) -> None:
        # для удобства сделаем матрицу иммутабельной
        # соответственно размерность у нас тоже всегда одинаковая
        self._matrix = matrix
        self._shape = self._calc_shape__() 
    
    @property
    def matrix(self):
        return self._matrix
    
    @property
    def shape(self):
        return self._shape
    
    def _calc_shape__(self):
        return (len(self.matrix), len(self.matrix[0]))
    
    def _get_matrix_col(self, j):
        return [row[j] for row in self.matrix]
    
    # декоратор для проверки размерности матриц, что бы не писать одинаковый код для всех методов
    # для того что бы он поддерживал аргумент пришлось сделать вложенность
    # transposed=True нужен для матричного умножения, когда у нас форма вида (10, 20) и (20, 10)
    # transposed=False нужен для поэтементного матричного умножения, когда у нас форма вида (10, 20) и (10, 20)
    def _shape_check(transposed=False): 
        def _shape_check_inner(method):
            def shape_checked(self, other):
                shape_other = other.shape[::-1] if transposed else other.shape
                if self.shape != shape_other:
                    raise ValueError(f'Matrix shape {self.shape} mismatch shape {other.shape} for this operation')
                else:
                    return method(self, other)
            return shape_checked
        return _shape_check_inner

    @_shape_check(transposed=False)
    def __add__(self, other: 'CustomMatrix'): # +
        new_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            new_row = [elem_a + elem_b for elem_a, elem_b in zip(row_a, row_b)]
            new_matrix.append(new_row)
        return CustomMatrix(new_matrix)
    
    @_shape_check(transposed=False)
    def __mul__(self, other):  # *
        new_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            new_row = [elem_a * elem_b for elem_a, elem_b in zip(row_a, row_b)]
            new_matrix.append(new_row)
        return CustomMatrix(new_matrix)
    
    @_shape_check(transposed=True)
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
        return CustomMatrix(new_matrix)
    
    
if __name__ == '__main__':
    np.random.seed(0)
    # [5 0 3 3 7]
    # [9 3 5 2 4]
    # [7 6 8 8 1]
    a_inner = np.random.randint(0, 10, (3, 5))
    # [6 7 7]
    # [8 1 5]
    # [9 8 9]
    # [4 3 0]
    # [3 5 0]
    b_inner = np.random.randint(0, 10, (3, 5))
    
    a = CustomMatrix(a_inner)
    b_1 = CustomMatrix(b_inner)
    b_2 = CustomMatrix(b_inner.T)
    
    # print(a_inner)
    # print(b_inner)
    
    c = a + b_1
    c_res = np.array(c.matrix)
    print(c_res)
    print(a_inner + b_inner)
    
    
    # d = a * b_1
    # e = a @ b_2

    # f = a + b_2
    # g = a * b_2
    # h = a @ b_1
    
    
