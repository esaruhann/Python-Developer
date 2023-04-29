
x = lambda a: a +  10

print(x(10))

#anonymous fınction

def myfun(n):
    
    return lambda a: a * n

my_doubler = myfun(2)
print(my_doubler(11))

li = [2, 5, 11, 22 ,35 ,44]
final_list = list(filter(lambda a: (a%2==0),li)) # filter takes 2 parameter, list and definition

final_list = list(map(lambda a: a*2,li)) # making process every element using map function
print(final_list)

from functools import reduce

sum = reduce((lambda x,y:x+y),li)

print(sum)

"""
1. Write a lambda function that takes two lists of integers and 
returns a new list with the maximum value for each index of the two lists.
 For example, given [1, 3, 5] and [2, 4, 6], the function should return [2, 4, 6].
 
 """
max_list = lambda list1, list2 : [list1[i] if list1[i] > list2[i] else list2[i] for i in range(min(len(list1), len(list2)))]


list1 = [1, 3, 5]
list2 = [2, 4, 6]
result = max_list(list1, list2)
print(result)

"""
2. Write a lambda function that takes a string of words separated by spaces, 
and returns a new string with the words in reverse order. For example, given the string "the quick brown fox",
 the function should return "fox brown quick the".
 """
 
reverse_words = lambda string: ' '.join(words for words in string.split())

input_string = "the quick brown fox"
result = reverse_words(input_string)
print(result)

"""
3. Write a lambda function that takes a string as input and returns True 
if the string is a palindrome (i.e., reads the same forward and backward), 
and False otherwise.
"""
pl = lambda string: True if string ==string[::-1] else False
pl = lambda string: True if string == ''.join(reversed(string))else False
print(pl("madam"))


#set() returns unique element

this_set = {"eda","arzu","arzu","mehmet"}
this_set.add("mustafa") # we cant use append
print(set(this_set))
z = this_set.pop()
print(z)

def gen_func():
    yield 1
    yield 2
    yield 3
    
x = gen_func()

print(next(x))
print(next(x))
print(next(x))

def fib(limit):
    a,b = 0,1
    
    while a <limit:
        yield a
        a,b = b,a+b
   
"""
Write a generator function that takes a list of numbers as input and yields only the even numbers.
"""

def even(number):
    for value in number:
        if value % 2 == 0:
            yield value
        
lst = [5, 10, 16, 17]
even_lst = list(even(lst))
print(even_lst)

"""
Write a generator function that takes a string as input and yields all the words in the string that start with a vowel.
"""
vowels = ['a', 'e', 'i', 'o', 'u']

def str_vowel(string):
    for word in string.split():
        if word[0].lower() in vowels:
            yield word

input_string = "eda saruhan"
vowel_words = list(str_vowel(input_string))
print(vowel_words)
        
"""
Write a lambda function that takes a list of dictionaries representing people,
 each with keys name and age, and returns a new list with the names of all the people over the age of 18.
 """
dic = {"eda":24,"seyma":25,"esra":15}
new_dict = lambda dic: [key  for key, value in dic.items() if value > 18]
print(new_dict(dic))