from fractions import Fraction as F
import Main 


def TB(Matrix:list) -> bool:
    """ Triangular bottom """
    
    check_TB: list = []
    LR: int = len(Matrix[0]) # lenght row in matrix
    
    for indx_r in range(LR -1):
        indx_cc = indx_r + 1
        check_r: list = []
        
        for indx_c in range(indx_cc, LR):
            num = Main.ATM(Matrix, indx_r, indx_c)
            
            if num == 0:
                check_r.append(True)
            else:
                return False
                break
        
        if all(check_r):
            check_TB.append(True)
        
    if all(check_TB):
        return True
    else:
        return False



def TT(Matrix:list) -> bool:
    """ Triangular top """
    
    check_TT: list = []
    
    for indx_r in range(1, len(Matrix)):
        check_r: list = []
        
        for indx_c in range(indx_r):
            num = Main.ATM(Matrix, indx_r, indx_c)

            if num == 0:
                check_r.append(True)
            else:
                return False
                break 
            
        if all(check_r):
            check_TT.append(True)
 
    if all(check_TT):
        return True
    else:
        return False
        


def D22(Matrix: list) -> int:
    """ Deterministic two by two """
    M1 = Matrix[0][0] * Matrix[1][1]
    M2 = Matrix[0][1] * Matrix[1][0]
    
    DE = M1 - M2
    return DE    



def Cafactor(row:int, col:int) -> int:
    """ Calculate cafactor """
    a = (row+1) + (col+1)
    
    if a % 2 == 0: return 1
    else : return -1
        


def Minor(Matrix: list, row: int, col: int) -> list:
    """ Delete selected row and column of numbers """
    L = len(Matrix)
    NM = []
    
    for i in range(L):
        if i == row: continue
        NR = []
            
        for j in range(L):
            if j == col: continue
            NR.append(Main.ATM(Matrix, i, j))
                
        NM.append(NR)

    return NM



def D33(Matrix: list, row:int =0) -> int:
    """ Deterministic three by three """
    D0: int = 0
    ln = len(Matrix)
    for c in range(ln):
        M0 = Minor(Matrix, row, c)
        M1 = Cafactor(row, c) * Main.ATM(Matrix, row, c)
        M2 = M1 * D22(M0)
        
        D0 += M2
    return D0
        


def tranhad(Matrix:list) -> list:
    
    LE = len(Matrix)
    MN = []
    
    for i in range(LE):
        col = Main.TC(Matrix, i)
        MN.append(col)
    
    return MN



def mul(Matrix:list, num:int) -> list:
    
    num = F(num, 1)
    print(num)
    MN = []
    for i in Matrix:
        NR = []
        
        for j in i:
            a = j * num 

            NR.append(a)
        MN.append(NR)
    return MN



def reverse(Matrix:list) -> list:
    """ Matrix inverse """
    
    det = D33(Matrix)
    
    if det == 0:
        exit(f"det matrix is:{det}")
        
    else:
        MN = []
        LE = len(Matrix)
        
        for i in range(LE):
            NR = []

            for j in range(LE):
                d1 = Minor(Matrix, j, i) 
                d2 = D22(d1)
                d3 = Cafactor(i, j) * d2
            
                NR.append(d3)
            
            MN.append(NR)

        det_reaverc = F(1/det)
        adj = tranhad(MN)
        return adj
        


if __name__ == "__main__":
    pass
    