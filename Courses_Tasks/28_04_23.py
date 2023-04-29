#new type class
"""
from dataclasses import dataclass

@dataclass

class Person():
    name: str = 'eda'
    age: int = 24
    height: float = 1.72

print(Person.name)

@dataclass
class People():
    people: list[Person]
    
    """
"""
Create a dataclass called Rectangle with the following attributes: 
    length (float), width (float), color (str).
    Write a method called area that returns the area of the rectangle.
    Instantiate an object of Rectangle with a length of 5.0, width of 3.0, and color of "blue", and print out its area.
"""
from dataclasses import dataclass

@dataclass

class Rectangle():
    length: float
    width: float
    color: str
 
@dataclass
class Area(Rectangle):
    def area(self):
        return self.length * self.width
    
rectangle = Area(length=5.0, width=3.0, color="blue")
print(rectangle.area())

"""
Create a dataclass called Student with the following attributes: name (str), id (int), grades (list of floats).
 Write a method called average_grade that returns the average of the student's grades. 
 Instantiate an object of Student with a name of "Alice", id of 12345, and grades of [3.5, 4.0, 3.7], and print out their average grade.
 """
from dataclasses import dataclass

@dataclass
class Student():
    name: str
    id: int
    grades: list
    def average_grade(self):
        return sum(self.grades)/len(self.grades)

student = Student(name="Alice", id=12345, grades=[3.5, 4.0, 3.7])
print(student.average_grade())

"""
Create a dataclass called Book with the following attributes:
 title (str), author (str), year (int), pages (int), rating (float), publisher (str), and genres (list of strings).
 Write a method called has_genre that takes a genre string as input and returns a boolean
 indicating whether the book belongs to that genre. Write a second method called to_dict that returns a dictionary of the book's attributes. 
 Instantiate several objects of Book with different attributes and test your has_genre and to_dict methods.
 """
 
from dataclasses import dataclass

@dataclass
class Book():
    title: str
    author: str
    year: int
    pages: int 
    rating: float
    publisher: str 
    genres: list
    def has_genre(self, genre: str):
       return genre in self.genres
    def to_dict(self):
       return f'Title is {self.title}, Author is {self.author}, Year is {self.year}, pages {self.pages}, rating is {self.rating}, publusher is {self.publisher} and genres are {self.genres}'
    
book = Book(title="Crime and Punishment", author="Fyodor Dostoevsky", year=1866, pages=430, rating=4.2, publisher="The Russian Messenger", genres=["fiction", "psychological thriller"])
print(book.has_genre("adventure"))
print(book.to_dict())




#Assert

assert sum([1,2,3]) == 6, "should be 6"

#unittest
import unittest
class TestSum(unittest.TestCase):
    def test_sum(self): # we have to start with test while class name is Test
        self.assertEqual(sum([1,2,3]),6,"Should be 6") # error message is optional
    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,3)),6,"Should be 6")
        
if __name__ == '__main__': # when we run the code as a main
    unittest.main()
    
"""
use unittest, re
define a valid email address

assertTrue
assertFalse
"""
import unittest
import re

def validemail(s):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, s))
    
    
class TestSum(unittest.TestCase):
    def test_email(self):
        self.assertTrue(validemail('edasaruhan21@ku.edu.tr'))
    def test_invalid(self):
        self.assertFalse(validemail('eda@saruhan21@ku.edu.tr'))

if __name__ == '__main__': # when we run the code as a main
    unittest.main()

    
