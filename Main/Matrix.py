import Main
import DeTerminal



def display():
    nama = """
┳┳┓        •    
┃┃┃ ┏┓ ╋ ┏┓┓ ┓┏
┛ ┗ ┗┻ ┗ ┛ ┗ ┛┗
                        
Please first select the desired operations
and then enter the number of rows and columns.  

[1]  Addition of two matrices.
[2]  Multiplication of two matrices.
[3]  Matrix determinant.
[4]  Matrix inverse.          

"""
    print(nama)


def input_user2():
    print("Matrix one >>")
    d11 = int(input("Enter Row: "))
    d12 = int(input("Enter colum: "))   
    m11 = []
    for x in range(d11):
        r = []
        for y in range(d12):
            a = int(input(f"a{x+1, y+1}: "))
            r.append(a)
        m11.append(r)
        
    print("Matrix tow >>")
    d21 = int(input("Enter Row: "))
    d22 = int(input("Enter colum: "))     
    m22 = []
    for i in range(d21):
        r = []
        for j in range(d22):
            a = int(input(f"b{i+1, j+1}: "))
            r.append(a)
        m22.append(r)
    print("=======================")
    return [m11, m22]


def input_user1():
    print("Matrix one >>")
    d11 = int(input("Enter Row: "))
    d12 = int(input("Enter colum: "))
            
    m11 = []
    for x in range(d11):
        r = []
        for y in range(d12):
            a = int(input(f"a{x+1, y+1}: "))
            r.append(a)
        m11.append(r)
    print("=======================")
    return m11



def choos():
    display()
    ch = int(input("Enter your optoin: "))
    
    match ch:
        case 1:
            matrice = input_user2()
            m = Main.MA(matrice[0], matrice[1])
            for i in m: print(i)
        case 2:
            matrice = input_user2()
            m = Main.MMS(matrice[0], matrice[1])
            for i in m: print(i)
        case 3:
            matrix = input_user1()
            m = DeTerminal.D33(matrix)
            print(m)
        case 4:
            matrix = input_user1()
            m = DeTerminal.reverse(matrix)
            for i in m: print(i)
            

if __name__ == "__main__":
    choos()