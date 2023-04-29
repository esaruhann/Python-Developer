"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myFun(self):
        return f"{self.name} {self.age}"
        
p1 = Person('Eda', 24)
print(p1.myFun())
"""

"""
 ex1 Create a Dog class with the following attributes: name, breed, and age. The class should also have the following methods: bark() and info().
 """
class Dog:
    def __init__(self,name,breed,age):
        self.name = name
        self.age = age
        self.breed = breed
        
    def bark(self):
        print("Hav Hav!")

    def info(self):
        print(f"{self.name} is a {self.breed} and {self.age} years old.")
    
my_dog = Dog('Cakir','Wolf','1')

my_dog.bark()
my_dog.info()
"""
ex2 Create a BankAccount class with the following attributes: balance and account_number. The class should also have the following methods: deposit(amount), withdraw(amount), and info().
"""
class BankAccount:
    def __init__(self,balance,account_number):
        self.balance = balance
        self.account_number = account_number
    def deposit(self,amount):
        self.balance-= amount
        print(f" New balance is {self.balance}.")
        
    def withdraw(self,amount):
        self.balance -= amount
        print(f" New balance is {self.balance}.")
    
    def info(self):
       print(f"account number: {self.account_number}\nBalance: {self.balance}")
       
acc = BankAccount(5000,679065280)
acc.deposit(100)
acc.withdraw(100)
acc.info()

#tupples, we cant add directly, we should convert them first list and smth and convert to tuple tuple = ('eda','saruhan')

List = [i**2 for i in [1,2,3]]
print(List)
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)
List = [i for i in 'Hello'] # we dont need external list and append comman
print(List)
"""
acc = print([[[num for num in range(100) if num %10 == 0] for j in range(100)]for i in range(100)])
print(acc)
    """    
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened_list = print([num for i in nested_list for num in i])
print(flattened_list)

"""
list1 = [1, 2]
list2 = [3, 4]
# Output: [(1, 3), (1, 4), (2, 3), (2, 4)]

"""
list1 = [1,2]
list2 = [3, 4]
print([(num1, num2) for num1 in list1 for num2 in list2])

"""
Write a list comprehension to find all the prime numbers between 1 and 100.
"""

print([num for num in range(2, 100) if all(num % i != 0 for i in range(2, num))])
