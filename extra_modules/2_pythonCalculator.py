

class Calculator:
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)

    def addition(self):
        print(self.a+self.b)

    def substructon(self):
        print(self.a-self.b)

    def multiply(self):
        print(self.a*self.b)

    def reminder(self):
        print(self.a%self.b)

class UserInput:
    Exp = '''
            this is a two digit calculator
            1 Addition 
            2 Substruction 
            3 multiply 
            4 devision            
    '''

    print(Exp)

    choice =  input('please enter your choice \t:')

    a = input('please enter first number\t:')
    b = input('please second numnber\t:')
    Calculator=Calculator(a,b)
    if (choice == '1'):

        result = Calculator.addition()

    elif (choice == '2'):

        result = Calculator.substructon()

    elif (choice == '3'):

        result = Calculator.multiply()


    elif (choice == '4'):

        result = Calculator.reminder()

    else:
        print('wrong input')

    print(result)

UserInput()
