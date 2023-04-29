"""
1.Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
(hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""
def payment(hour,rate):
    
    if isinstance(hour,str) or isinstance(rate,str):
        raise Exception("Input should not be string")
    if int(hour)<=40:
        pay_result =int(hour)*int(rate)
        return pay_result
        
    elif  int(hour) > 40:
        pay = 40 * rate
        pay2 = ( int(hour) - 40)*rate*1.5
        pay_result = pay + pay2
        return pay_result

print(payment(45,10))
    
"""
2.2.Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
"""
def computegrade(score):
     try:
         if score<0 or  score>1:
            print("score is out of range")
         elif score >= 0.9:
             grade = "A"
             return grade
         elif score >= 0.8:
             grade = "B"
             return grade
         elif score >= 0.7:
             grade = "C"
             return grade
         elif score >= 0.6:
             grade = "D"
             return grade
         elif score < 0.6:
             grade = "F"
             return grade   
     except ValueError:
         print("score should ve float")
     except:
         print("score is out of range")

score = float(input("Enter your score: "))
computegrade(score)


"""

# problem
print('Good morning!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')
print('Good afternoon!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')
print('Good evening!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')

"""
list_ = ("morning!", "afternoom!","evening")
def feeling(*args):
    for arg in args:
        print("Good ",arg)
        print('How are you feeling?')
        feeling = input()
        print('I am happy to hear that you are feeling ' + feeling + '.')
feeling(*list_)    

"""
1.Write a program which repeatedly reads numbers until the
user enters `done`. Once `done` is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333

functions to be used:

from statistics import mean
sum() - len() - sum()/len() - mean()
"""
total = 0
count = 0
avg = 0
while True:
    try:
        number = (input("Enter number: "))
        if number == "done":
            print( total, count, avg)
            break
        total = total + float(number)
        count = count + 1
        avg = total/count
    except:
        print("invalid number")

        
