
class Deductions:
    
    def simplify(a:list) -> list:
        if a[0] < 0 > a[1]:
            a = [abs(a[0]), abs(a[1])]
                 
        for num in range(2, 9):
            if a[0] % num == 0 :
                if a[1] % num == 0:
                    a[0] = int(a[0]/num)
                    a[1] = int(a[1]/num)
        return a
    
    
    def plural(a:list, b:list) -> list:
        if a[1] == b[1]:
            sum = a[0] + b[0]
            return [sum, a[1]]
        else:
            d  = a[1] * b[1]
            ab = a[0] * b[1]
            bb = b[0] * a[1]
            
            sum = ab + bb
            return Deductions.simplify([sum, d])
        
    
    def multiplication(a:list, b:list) -> list:
        form = a[0] * b[0]
        port = a[1] * b[1]
        return Deductions.simplify([form, port])
    
    
    def division(a:list, b:list) -> list:
        form = a[0] * b[1]
        port = a[1] * b[0]
        return Deductions.simplify([form, port])    
        
        
if __name__ == "__main__":
    print(Deductions.simplify([6, -27]))
    pass