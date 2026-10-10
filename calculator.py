# 15 December 2025

class Calculator :
    
    PI = 3.14
    def _init_(self, button):
        self.button = button

    def addition (self, Limit):
        '''You select addition: '''
        sum = 0
        for i in range(1, Limit+1):
            num = int(input(f"Enter your number{i}: "))
            sum += num
            print(f"Result = {sum}")

    @staticmethod
    def subtraction():
        '''You select subtraction (-)'''
        subtract = 0
        num1 = int(input(f"Enter number1: "))
        num2 = int(input(f"Enter number2: "))
        subtract =  num1 - num2
        print(f"Result = {subtract}")

    def multiplication (self, Limit):
        '''You select multiplication:'''
        multiple = 1
        for i in range(1, Limit+1):
            num = int(input(f"Enter your number{i}: "))
            multiple *= num
            print(f"Result = {multiple}")

    @staticmethod
    def division():
        '''You select division(/)'''
        dividend = int(input(f"Enter number which you want to divide: "))
        divisor = int(input(f"Enter number by which you want to divide: "))
        if(divisor == 0):
            print("Value Error: Division by zero (0) is not allowed: ")
        else:
            quotient =  dividend / divisor
            ans = round(quotient, 3)
            remainder = dividend % divisor
            print(f"Result of {dividend}/{divisor} is: \nQuotient = {ans}\nRemainder = {remainder}")

    def square(self, base):
        '''You select square(b^2)'''
        Result = base ** 2
        print(f"Square of {base} = {Result}")

    def square_root(sefl, base):
        '''You select the square_root'''
        sqrt = base ** 0.5
        print(f"Square-root of (base) = {sqrt}")

    def cube(self, base):
        '''You select cube(b^3)'''
        Result = base ** 3
        print(f"Cube of (base) = {Result}")

    def cube_root(self, base):
        '''You select the cube_root'''
        cube_rt = base ** (1/3)
        print(f"Cube-root of (base) = round{(cube_rt)}")

    def power_of_num():
        power = int(input("Enter the power: "))
        base  = int(input("Eneter the base : "))
        result = base ** power
        print(f"Result: \n{base}^{power} = {result}")

    @staticmethod
    def num_ten_raise_power():
        '''You select num x 10^ n'''
        base = 10
        num = int(input("Enter number you want to multiply with 10^n: "))
        power = int(input("Enter the power: "))
        result = num * 10 ** power
        print(f"Result: \n{num} x 10^ {power} = {result}")

    def multi_with_pi(self, num):
        '''You select multi_with_pi'''
        Result = self.PI * num
        print(f"{num} x {self.PI} = {Result}")

    def factorial(self,num):
        '''You select factorial (num!)'''
        fact = 1
        for i in range(1, num+1):
            fact *= i

        print(f"Result : {num}! = {fact}")


button = input("Enter button (on/off) to on or off calculator: ")
c1 = Calculator (button)
if(button== "on"):
    # This is a list of Actions which this calculator can perform
    List = ["addition", "subtraction", "multiplication", "devision",
            "square", "square_root", "cube", "cube_root", "power_of_num",
            "ten_raise_power", "multi_with_pi", "factorial"]
    # This show the user all actions and ask the user to chose any one among them
    for option in List:
        print(option)
    else:
        Action = input("Which action you want to do from following: ")
        # The flow of operations
        # The flow of operations
        if(Action == "addition" or Action == '+'):
            print(c1.addition._doc_)
            Limit = int(input("How many number you want to add : "))
            c1.addition(Limit)

        elif (Action == "subtraction" or Action == "-"):
            print(c1.subtraction._doc_)
            c1.subtraction()

        elif(Action == "multiplication" or Action == "x"):
            print(c1.multiplication._doc_)
            Limit = int(input("How many number you want to multiply: "))
            c1.multiplication(Limit)

        elif (Action == "division" or Action == "/"):
            print(c1.division._doc_)
            c1.division()

        elif(Action == "square" or Action == "^2"):
            print(c1.square._doc_)
            base = int(input("Enter the number of which you want to take square: "))
            c1.square(base)

        elif(Action == "square_root" or Action == "sqrt"):
            print(c1.square_root._doc_)
            base = int(input("Enter the number of which you want to take square-root: "))
            c1.square_root(base)

        elif (Action == "cube" or Action == "^3"):
            print(c1.cube._doc_)
            base = int(input("Enter the number of which you want to take cube: "))
            c1.cube(base)

        elif (Action == "cube_root" or Action == "cube_rt"):
            print(c1.cube_root._doc_)
            base = int(input("Enter the number of which you want to take cube-root: "))
            c1.cube_root(base)

        elif(Action == "b^n" or Action == "power_of_num"):
            print(c1.power_of_num._doc_)
            c1.power_of_num()

        elif(Action == "num_ten_raise_power" or Action == "10^n"):
            print(c1.num_ten_raise_power._doc_)
            num = int(input("Enter number you want to multiply with pi: "))
            c1.multi_with_pi(num)

        elif (Action == "factorial" or Action == "fact"):
            print(c1.factorial._doc_)
            num = int(input("Enter number for factorial: "))
            c1.factorial(num)
        else:
            print("Please enter a valid action: ")
            
elif(button == "off"):
    print("OFF")