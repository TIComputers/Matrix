from Main import *
from Examples import *
from time import sleep, time

def MMS(Matrix1:list, Matrix2:list) -> list:
    """ Multiply matrices systematically """
    RC1 = NRC(Matrix1)
    RC2 = NRC(Matrix2)
    
    if RC1[0] != RC2[1]: # red line
            exit(f"Cann`t Multiply matrix -> {RC1} * {RC2}")

    NM = [] # new matrix for multiply matrix1 to matrix2

    for row in Matrix1: # row is a list from Matrix1
        NR = [] # new row form New Matrix
        for col in range(RC2[1]):
            Col = TC(Matrix2, col)
            sum = 0
            for i in range(RC1[1]):
                mul = 0
                mul = row[i] * Col[i]
                sum += mul
            NR.append(sum)
        NM.append(NR)
    return NM
        
        
start = time()
print(MMS(matrix_10x10_a, matrix_10x10_b))
stop  = time()
print(f"Time: {stop - start}")
