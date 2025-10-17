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
        

def DTT():
    """ Deterministic two by two """
    pass


def Minor():
    pass


def Cafactor():
    """ Calculate cafactor """
    pass



