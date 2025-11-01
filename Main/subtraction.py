
class Deductions:
    
    def plural(a:list, b:list) -> list:
        if a[1] == b[1]:
            sum = a[0] + b[0]
            return [sum, a[1]]
        else:
            d  = a[1] * b[1]
            ab = a[0] * b[1]
            bb = b[0] * a[1]
            
            sum = ab + bb
            return  [sum, d]
        
    
    def multiplication(a:list, b:list) -> list:
        form = a[0] * b[0]
        port = a[1] * b[1]
        return [form, port]
    
    
    def division(a:list, b:list) -> list:
        form = a[0] * b[1]
        port = a[1] * b[0]
        return [form, port]    
        
        
if __name__ == "__main__":
    pass