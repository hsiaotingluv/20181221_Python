#example 1 - encapsulation - class

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark")

    def add_one(self, x):
        return x + 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

d = Dog("Tim", 34)
d2 = Dog("Bill", 12)
print(d2.get_age())
print(d2.get_name())
d2.set_age(23)
print(d2.get_age())





#example 2
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

science = Course("Science", 2)
science.add_student(s1)
science.add_student(s2)
print(science.add_student(s3))
print(science.get_average_grade())





#example 3 - inheritant - parent class and child class

class Pet: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) #inherent from parent initialisations
        self.color = color

    def speak(self): #overwrites parent class
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self): #overwrites parent class
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34, "Brown")
c.show()
d = Dog("Jill", 25)
d.show()

c.speak()
d.speak()

f = Fish("Bubbles", 10)
f.speak()





# example 4 - class attributes, export to other files easily

class Person:
    number_of_people = 0 #class attributes

    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Tim")
print(Person.number_of_people)
p2 = Person("Jill")
print(Person.number_of_people)

Person.number_of_people = 8
print(p2.number_of_people)
print(Person.number_of_people)

print(Person.number_of_people_())





#example 5 - static method

class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def pr():
        print("run")

print(Math.add5(5))
Math.pr()