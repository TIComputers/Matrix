from time import time, sleep
from test2 import *

def ATM(Matrix:list, row:int, col:int) -> int:
    I = Matrix[row]
    a = I[col]
    return a


def NRC(Matrix:list) -> str:
    """ Number of rows and columns,
        Order of the matrix """
    # number of row in matris
    row = 0
    for i in Matrix:
        row += 1

    # number of column in matris
    col = 0
    for j in Matrix[1]:
        col += 1

    return (row, col)


def MDS (Matrix:list) -> bool:
    """ Matrix defines structure
        Columns per row """
    RL = []   # length row
    
    for row in Matrix:   # Getting the number of items in each row
        L = len(row)
        RL.append(L) 
          
    for time in RL: # Checking for equality of items
        if time != L:
            exit("Your list is not a Matrix")

  
    
def NRC(Matrix:list) -> str:
    """ Number of rows and columns,
        Order of the matrix """
    # number of row in matris
    row = 0
    for i in Matrix:
        row += 1

    # number of column in matris
    col = 0
    for j in Matrix[1]:
        col += 1
        
    return (row, col)


def MA(Matrix1:list, Matrix2:list) -> list:
    """ Matrix Addition """
    RC1 = NRC(Matrix1)
    RC2 = NRC(Matrix2)

    if RC1 != RC2:  # red line
        exit(f"Cann`t Adding Matrix1{RC1} with Matrix2{RC2}")
    
    NM = [] # new matrix for addition matrix1 to matrix2
    
    for i in range(RC1[0]):
        NR = [] # new row for new matrix
        for j in range(RC1[1]):
            sum = ATM(Matrix1, i, j) + ATM(Matrix2, i, j)
            NR.append(sum)
        NM.append(NR)
    return NM


def TC(Matrix:list, col:int) -> list:
    """ The columns """

    columns = [] # new list for write columns list
    for row in Matrix:
        columns.append(row[col])
    return columns


def MMS(Matrix1:list, Matrix2:list) -> list:
    """ Multiply matrices systematically """
    RC1 = NRC(Matrix1)
    RC2 = NRC(Matrix2)
    
    if RC1[0] != RC2[1]: # red line
            exit(f"Cann`t Multiply matrix -> {RC1} * {RC2}")

    NM = [] # new matrix for multiply matrix1 to matrix2
 
    for row in Matrix1:
        NR = [] # new row for add new matrix multiplyed
        for col in range(RC2[1]):
            COL = TC(Matrix2, col)
            sum = 0
            for i in range(RC2[1]):
                mul = 0
                mul = row[i] * COL[i]
                sum += mul
            NR.append(sum)
        NM.append(NR)
    return NM
        



