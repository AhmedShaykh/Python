# class Teacher:

#     def __init__(self, teacherId : int, teacherName : str) -> None: # Method / Constructor (__Init__)

#         self.name : str = teacherName; # Attribute

#         self.teacherId : int  = teacherId;

#         self.organizationName: str = "PIAIC";

#     def quarter(self, quarter : int ) -> None: # Method

#         print(f"This Is Quarter {quarter}");
    
#     def teaching(self, subject : str ) -> None:

#         print(f"{self.name} Is Teaching {subject}...!");

# obj1 : Teacher = Teacher(1, "Sir Zia Khan");

# obj2 : Teacher = Teacher(2, "Sir Qasim");

# print(f"Name: {obj1.name}, ID: {obj1.teacherId} & Organiztion: {obj1.organizationName} \n");

# print(f"Name: {obj2.name}, ID: {obj2.teacherId} & Organiztion: {obj2.organizationName} \n");

# obj1.teaching("BlockChain")

# obj2.teaching("Generative AI")

# print(dir(obj1));

# class Teacher:

#     counter : int = 0; # Variable

#     classTiming : str = "8 PM";

#     def __init__(self, teacherId : int, teacherName : str) -> None:

#         self.name : str = teacherName;

#         self.teacherId : int  = teacherId;

#         self.organizationName: str = "PIAIC";
    
#         Teacher.counter += 1;

#     def quarter(self, quarter : int ) -> None:

#         print(f"This Is Quarter {quarter}");
    
#     def teaching(self, subject : str ) -> None:

#         print(f"{self.name} Is Teaching {subject}...!");

#     def details(self) -> None:

#         information : str = f"""
#         Teacher Name Is {self.name}
#         Class Timing is {Teacher.classTiming}
#         """;
        
#         print(information);

# print(Teacher.counter);

# obj1 : Teacher = Teacher(1, "Sir Zia Khan"); # Create New Object Then Increase The Value Of Counter

# print(obj1.counter); # And Also Run The Object Increase The Value Of Counter

# print(obj1.counter);

# print(Teacher.counter);

# obj2 : Teacher = Teacher(2, "Sir Qasim");

# print(obj1.counter);

# print(obj2.counter);

# print(Teacher.counter);

# obj1.details();

# print(id(obj2));

# ================== Inheritance ================== #

class Parents():

    def __init__(self) -> None:

        self.eyeColor : str = "Brown";

        self.hairColor : str = "Black";

    def speak(self, words: str) -> None:

        print(f"Parent Method Speak: {words}");

    def watching(sef, objectName : str) -> None:

        print(f"You Are Looking {objectName}");

class Child(Parents):

    pass;

obj1 : Parents = Parents();

print(obj1.eyeColor);

print(obj1.hairColor);

obj1.speak("Pakistan Zindabad");

obj1.watching("TV \n");

obj2 : Child = Child();

obj2.speak("Free Palestine");

obj2.watching("Youtube");

print(obj2.eyeColor);

print(obj2.hairColor);

class Parents():

    def __init__(self) -> None:

        self.eyeColor : str = "Brown";

        self.hairColor : str = "Black";

    def speak(self, words: str) -> None:

        print(f"Parent Method Speak: {words}");

    def watching(sef, objectName : str) -> None:

        print(f"You Are Looking {objectName}");

class Child(Parents):

    def music(self, genre : str) -> None:

        print(f"I Love {genre}");

obj1 : Parents = Parents();

print(obj1.eyeColor);

print(obj1.hairColor);

obj1.speak("Pakistan Zindabad");

obj1.watching("TV \n");

obj2 : Child = Child();

obj2.speak("Free Palestine");

obj2.watching("Youtube");

print(obj2.eyeColor);

print(obj2.hairColor);

obj2.music("EDM");

from typing import List;

class Employee():

    def __init__(self, name : str) -> None:

        self.name : str = name;

class Designer(Employee):
    
    def __init__(self, title : str, name: str) -> None:

        super().__init__(name);

        self.title : str = title;

class Developer(Employee):

    def __init__(self, title : str, name: str) -> None:

        super().__init__(name);

        self.title: str = title;
        
        self.programming_skills : List[str] = ["JavaScript", "TypeScript", "Python"];

design: Designer = Designer("Animation Artist", "Ahsan");

dev: Developer = Developer("Gen AI Engineer", "Ahmed");

print(design.name);

print(design.title);

print(dev.title);

print(dev.programming_skills);

class Mother:

    def __init__(self, name: str) -> None:

        self.name : str = name;

        self.eyeColor : str = "Blue";

class Father:

    def __init__(self, name: str) -> None:

        self.name : str = name;

        self.height : str = "7 Feet";

class Child(Mother, Father):

    def __init__(self, motherName: str, fatherName: str ,childName: str) -> None:

        Mother.__init__(self, motherName);

        Father.__init__(self, fatherName);

        self.childName : str = childName;

    def speaking(self, words: str) -> str:

        return f"Imran Khan Speaking: {words}";

imran : Child = Child("Shaukat Khanum", "Ikramullah Khan","Imran Khan");

print(f"Imran Khan Height {imran.height}");

print(f"Imran Khan Eye Color {imran.eyeColor}");

print(imran.speaking("Absolutely Not"));

print([i for i in dir(imran) if "__" not in i]);

from typing import Union, overload;

@overload #Overload
def add(self, x: int, y: int) -> int:
    ...

@overload
def add(self, x: float, y: float) -> float:
    ...
        
@overload
def add(self, x: str, y: str) -> str:
    ...

def add(x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
    if isinstance(x, int) and isinstance(y, int):
        return x + y;
    elif isinstance(x, float) and isinstance(y, float):
        return x + y;
    elif isinstance(x, str) and isinstance(y, str):
        return x + y;
    else:
        raise TypeError("Invalid Argument Types!");

result1 = add(1, 2);

result2 = add(2.5, 2.5);

result3 = add("Hello", " World!");

print(result1);

print(result2);

print(result3);

class Adder:

    @overload
    def add(self, x: int, y: int) -> int:
        ...

    @overload
    def add(self, x: float, y: float) -> float:
        ...
        
    @overload
    def add(self, x: str, y: str) -> str:
        ...

    def add(self, x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
        if isinstance(x, int) and isinstance(y, int):
            return x + y;
        elif isinstance(x, float) and isinstance(y, float):
            return x + y;
        elif isinstance(x, str) and isinstance(y, str):
            return x + y;
        else:
            raise TypeError("Invalid Argument Types!");

adder: Adder = Adder();

result1 = adder.add(2, 2);

result2 = adder.add(2, 2);

result3 = adder.add("Free", " Palestine!");

print(result1);

print(result2);

print(result3);

# ================== Polymorphism ================== #

class Animal():

    def eating(self, food: str ) -> None:

        print(f"Animal Is Eating {food}");

class Bird(Animal):

    def eating(self, food: str) -> None:

        print(f"Bird Is Eating {food}"); # OverRide

bird : Bird = Bird();

bird.eating("Bread");

animal : Animal = Animal();

animal.eating("Grain");

print(type(animal));

animal2 : Animal = Bird(); # Object Will Decide Which Object Method It Will Be Run

animal2.eating("Seeds");

print(type(animal2));

bird2 : Bird = Animal(); # It's Called Polymorphism

bird2.eating("Seeds");

class Mother:

    def __init__(self, name: str) -> None:

        self.name : str = name;

        self.eyeColor : str = "Blue";

    def speaking(self, words: str) -> str:

        return f"Imran Khan Mother Speaking: {words}";

class Father:

    def __init__(self, name: str) -> None:

        self.name : str = name;

        self.height : str = "7 Feet";

    def speaking(self, words: str) -> str:

        return f"Imran Khan Father Speaking: {words}";

class Child(Father, Mother):

    def __init__(self, motherName: str, fatherName: str ,childName: str) -> None:

        Mother.__init__(self, motherName);

        Father.__init__(self, fatherName);

        self.childName : str = childName;

imran : Child = Child("Shaukat Khanum", "Ikramullah Khan","Imran Khan");

print(f"Imran Khan Height {imran.height}");

print(f"Imran Khan Eye Color {imran.eyeColor}");

print(imran.speaking("Pakistan Zindabad!"));

class MathOperations:

    organization : str = "PIAIC";

    @staticmethod # Static Method
    def add(x: int, y: int) -> int:

        return x + y;

    @staticmethod
    def multiply(x: int, y: int) -> int:
    
        return x * y;

resultAdd = MathOperations.add(10, 20); # In Static Method & Variable Direct Access To Variable & Method With Class Name

resultMultiply = MathOperations.multiply(10, 20); # No Need Create The Object

print("Addition:", resultAdd);

print("Multiplication:", resultMultiply);

print(MathOperations.organization);

class Bilal():

    def eating(self, food : str) -> None:

        print(f"Bilal is Eating {food}");
    
obj1 : Bilal = Bilal();

obj1.eating("Biryani");

print(dir(obj1)); # Everything Is An Object In Python

print(dir(object));

class Ahmed(object):

    def drinking(self, drink : str) -> None:

        print(f"Human is Drinking {drink}");
    
obj2 : Ahmed = Ahmed();

obj2.drinking("Tea");

print(dir(obj2));

def greet(): # Callable
    
    print("Martin Garrix");

greet.__call__(); # Callable Method Is Built-In Method In Every Object

print(dir(greet));

class MainWindow:

    def show(self):

        print("Showing The App Main Window...");

    def __call__(self):

        self.show();

window = MainWindow();

window(); # Callable Is Built-In Method So I Not Give The Method Name But It Run

class Human(object):

    def eating(self, food : str) -> None:

        print(f"Human Is Eating {food}");

    def __call__(self) -> None: # Default Run

        self.eating("Nihari!");

obj : Human = Human();

obj();

obj.eating("Biryani");

print(type(Human));

print(dir(type)); # Call Method Is Built-In In Every Object

class SampleClass:
     
     def method(self):
         
         print("You Called Method!");

sampleInstance = SampleClass();

print(dir(sampleInstance.method)); # Show All Object Method's

class NonCallable:

    def __call__(self):

        raise TypeError("Not Really Callable");
    
instance : NonCallable = NonCallable();

print(callable(instance));

print(callable(NonCallable));

class PowerFactory:

    def __init__(self, exponent: int = 2):

        self.exponent = exponent;

    def __call__(self, base: int):

        return base ** self.exponent;
    
a : PowerFactory = PowerFactory(); # Run __init__

print(a.exponent);

print(a(8));

class CumulativeAverager:

    def __init__(self):

        self.data = [];

    def __call__(self, newValue):

        self.data.append(newValue);

        print(self.data);

        return sum(self.data) / len(self.data);

streamAverage = CumulativeAverager();

print(streamAverage.data);

print(streamAverage(12)); # Data = [12] (12/1)

print(streamAverage(13)); # Data = [12, 13] (12 + 13 / 2)

print(streamAverage(11));

print(streamAverage(10));

class Factorial:

    def __init__(self):

        self.cache = {0: 1, 1: 1};

    def __call__(self, number):

        if number not in self.cache:

            self.cache[number] = number * self(number - 1);
        
        return self.cache[number];

factorialOf = Factorial();

print(factorialOf.cache);

factorialOf(4);

factorialOf(5);

factorialOf(4);

factorialOf(10);

print(factorialOf.cache);

from package.pack import ExecutionTimer; # Module

@ExecutionTimer

def squareNumbers(numbers):

    return [number ** 2 for number in numbers];

print(squareNumbers(list(range(10))));