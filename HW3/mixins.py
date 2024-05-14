import re

class ShapeCheckMixin:
    """
    Декоратор для проверки размерности матриц, что бы не писать одинаковый код для всех методов.  
    Для того что бы он поддерживал аргумент пришлось сделать вложенность.
    

    transposed=True нужен для матричного умножения, когда у нас форма вида (10, 20) и (20, 10)\n
    transposed=False нужен для поэлементного матричного умножения, когда у нас форма вида (10, 20) и (10, 20)
    """
    def _shape_check(transposed=False): 
        def _shape_check_inner(method):
            def shape_checked(self, other):
                shape_other = other._shape[::-1] if transposed else other._shape
                if self._shape != shape_other:
                    raise ValueError(f'Matrix shape {self._shape} mismatch shape {other._shape} for this operation')
                else:
                    return method(self, other)
            return shape_checked
        return _shape_check_inner


class PrintMixin:
    # Красивый вывод в строку
    def __str__(self) -> str:
        return "\n".join([re.sub("[\[\],]","",str(row)) for row in self._matrix])


class SubstractionMixin(ShapeCheckMixin):
    # Вычитание
    @ShapeCheckMixin._shape_check(transposed=False)
    def __sub__(self, other):
        new_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            new_row = [elem_a - elem_b for elem_a, elem_b in zip(row_a, row_b)]
            new_matrix.append(new_row)
        return self.__class__(new_matrix)
    
class DivisionMixin(ShapeCheckMixin):
    # Деление 3-х видов
    @ShapeCheckMixin._shape_check(transposed=False)
    def __truediv__(self, other):
        new_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            new_row = [elem_a / elem_b for elem_a, elem_b in zip(row_a, row_b)]
            new_matrix.append(new_row)
        return self.__class__(new_matrix)
    
    @ShapeCheckMixin._shape_check(transposed=False)
    def __floordiv__(self, other):
        new_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            new_row = [elem_a // elem_b for elem_a, elem_b in zip(row_a, row_b)]
            new_matrix.append(new_row)
        return self.__class__(new_matrix)
    
    @ShapeCheckMixin._shape_check(transposed=False)
    def __mod__(self, other):
        new_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            new_row = [elem_a % elem_b for elem_a, elem_b in zip(row_a, row_b)]
            new_matrix.append(new_row)
        return self.__class__(new_matrix)


class PropertyMixin:
    # Геттеры и сеттеры
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


class SaveMixin:
    # запсиь в файл
    def save(self, file_path):
        with open(file_path, 'wt') as outfile:
            outfile.write(str(self))
        
    