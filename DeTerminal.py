import Main


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
                check_r.append(False)
            
        if all(check_r):
            check_TT.append(True)
        else: 
            check_TT.append(False)
 
    if all(check_TT):
        return True
    else:
        return False
        

        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


def TB():
    """ Triangular bottom """
    pass

























def DTT():
    """ Deterministic two by two """
    pass


def Minor():
    pass


def Cafactor():
    """ Calculate cafactor """
    pass



