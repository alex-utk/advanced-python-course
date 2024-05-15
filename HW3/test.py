import numpy as np
from matrix_class import SuperCustomMatrix

    
def main():
    np.random.seed(0)
    # [6 1 4 4 8]
    # [4 6 3 5 8]
    # [7 9 9 2 7]
    a_inner = np.random.randint(1, 10, (3, 5))
    # [8 8 9 2 6]
    # [9 5 4 1 4]
    # [6 1 3 4 9]
    b_inner = np.random.randint(1, 10, (3, 5))
    
    a = SuperCustomMatrix(a_inner)
    a.save(r'HW3\artefacts\input_a.txt')
    b = SuperCustomMatrix(b_inner)
    b.save(r'HW3\artefacts\input_b.txt')
    b_t = SuperCustomMatrix(b_inner.T)


    # под капотом у save используется str
    (a * b).save(r'HW3\artefacts\matrix+.txt')
    (a * b).save(r'HW3\artefacts\matrix_mul.txt')
    (a @ b_t).save(r'HW3\artefacts\matrix@.txt')
    (a - b).save(r'HW3\artefacts\matrix-.txt')
    (a / b).save(r'HW3\artefacts\matrix_true_div.txt')
    (a // b).save(r'HW3\artefacts\matrix_floor_div.txt')
    (a % b).save(r'HW3\artefacts\matrix_mod.txt')
    
    print(a) # тут сработает str
    
    
if __name__ == '__main__':
    main()
    