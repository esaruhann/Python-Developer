#q1
inp_1 = input("write your name: ")
print(f'welcome {inp_1}')

#q2

hour =input("Enter Hour ")
rate = input("Enter rate") 

             
def pay(x,y):
    
    return float(x)*float(y)

print(pay(hour,rate))

#q3
cel = float(input("Enter celcius"))

print("fahrenheit = ", cel*1.8+32)

#q4

hour =input("Enter Hour ")
rate = input("Enter rate") 
if int(hour)<=40:
    pay_result =int(hour)*int(rate)
    
elif  int(hour) > 40:
    pay = 40 * int(rate)
    pay2 = ( int(hour) - 40)*int(rate)*1.5
    pay_result = pay + pay2
    
print(pay_result)

#q5
"""
2.Write a program to prompt for a score between 0.0 and
1.0. If the score is out of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table:

Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
"""
try:
    score = float(input("Enter your score: "))
    if score<0 or  score>1:
       print("score is out of range")
    elif score >= 0.9:
        print("your score is A")
    elif score >= 0.8:
        print("your score is B")
    elif score >= 0.7:
        print("your score is C")
    elif score >= 0.6:
        print("your score is D")
    elif score < 0.6:
        print("your score is F")    
except ValueError:
    print("score should ve float")
except:
    print("score is out of range")
    
    

