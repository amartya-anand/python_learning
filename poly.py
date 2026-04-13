#Method Overriding

class Add: 

    def result(self, a, b): 
        print('Addition:', a+b) 

class Multi(Add): 

    def result(self, a, b): 
        print('Multiplication:', a*b) 


m = Multi() 

m.result(10, 20) 

# Super 

class Add: 

    def result(self, a, b): 
        print('Addition:', a+b) 

class Multi(Add): 

    def result(self, a, b): 
        # Calling Parent Class's Method 

        super().result(30, 50) 
        print('Multiplication:', a*b) 

m = Multi() 

m.result(10, 20) 