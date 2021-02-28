# declaring class and using oops concepts

class Employee:

    #declaring class varianble
    no_of_emps = 0
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first =  first
        self.last =  last
        self.pay = pay
        self.email = first+last+'@testmail.com'

        Employee.no_of_emps += 1

    def fullname(self):
        fullname = self.first + ' '+ self.last
        return fullname

    def apply_raise(self):
        self.pay = float(self.pay) * float(self.raise_amt)

    @classmethod
    def set_raise_amout(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def split_from_string(cls,inp_str):
        first,last,pay = inp_str.split('-')

        return cls(first,last,pay)
    
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay,pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang

class Manager(Employee):
    raise_amt = 1.12

    def __init__(self, first, last, pay,employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []

        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


    

        


emp1 = Employee('jeetendra','kumar','60000')
emp2 = Employee.split_from_string('raja-H-70000')

dev1 = Developer('lokesh','singh',75000,'python')

man1 = Manager('Dina','Ravinderan',100000,[dev1,emp1,emp2])
print(emp1.fullname())
print(emp1.email)

print(dev1.email)
print(dev1.apply_raise())
print(dev1.pay)
print(emp2.fullname())
emp2.set_raise_amout(1.05)
emp2.apply_raise()
print(emp2.pay)
print(emp2.no_of_emps)

import datetime

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
man1.remove_emp(emp2)
print (man1.print_emps())