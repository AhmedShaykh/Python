from typing import List;

x: int = 10;

print("Before Modification:", x, id(x));

x += 1;

print("After Modification:", x, id(x));

a : List[str] = ["A","B"];

b : List[str] = ["C","D"];

print(id(a));

print(id(b));

print(a + b);

print(15 - 7);

num: int = 5; # Immutable

def myNum(num: int) -> None:

    num = 6;

    print(num);

myNum(num); # Pass By Value Immutable

print(num);

num: List[int] = [1, 2, 3, 4]; # Mutable

def myNum(num: List[int]) -> None:

    num.append(200); # Added On Element

    print(f"Number 2 Value Is {num}");

myNum(num); # Pass By Reference (Mutable Data Type)

print(num);

num: List[int] = [1, 2, 3, 4];

print(id(num));

def myNum(num: List[int]) -> None:

    print(f"Start Of Function {num} & Its Address: {id(num)}");

    num.append(200);

    print(f"End Of Function {num} & Its Address: {id(num)}"); # Because Its A Mutable Value Then It Same 

myNum(num);

print(num);

num: List[int] = [1, 2, 3, 4];

def myNum(num: List[int]) -> None:

    num: List[int] = [1, 2, 3, 4, 5];

    num.append(200);

    print(f"Number 2 Value Is {num}");

myNum(num);

print(num);

name: list[str] = ["Ahmed", "Ahmëd", "AHM X"];

indx: int = int(input("Enter Index Number:"));

print(name[indx]);

print("Logic 1");

print("Logic 2");

try:

    print(5 / 0);

except ZeroDivisionError:
    
    print("Zero Division Error!");

print("Logic 4");

print("Logic 5");

print("Logic 1");

print("Logic 2");

li : list[int] = [1, 2, 3];

try:

    print(5 / 0);

    li[0] = 23; # Mutable Value Not Change

    print(xyz); # Variable Not Exist

except (ZeroDivisionError, IndexError, NameError):
    
    print("Error!");

print("Logic 4");

print("Logic 5");

print("Logic 1");

print("Logic 2");

li : list[int] = [1, 2, 3];

try:

    print(5 / 2);

    print(li[4]); # Error

    print(z);

except (ZeroDivisionError):
    
    print("Zero Division Error!");

except IndexError:

    print("Index Error");

except NameError:

    print("Name Not Defined");

print("Logic 4");

print("Logic 5");

print("Logic 1");

print("Logic 2");

li : list[int] = [1, 2, 3];

try:

    print(5 / 2);

    print(li[1]);

    print(li);

    open("app.py");

except (ZeroDivisionError):
    
    print("Zero Division Error!");

except IndexError:

    print("Index Error");

except NameError:

    print("Name Not Defined");

except:

    print("Something Went Wrong!");

print("Logic 4");

print("Logic 5");

try:
    
    print(li[200]);

except Exception as e:

    print(f"Something Went Wrong!\n{e}");

data = open("./app.txt");

print(data);

from typing import TextIO;

data: TextIO = open("./app.txt"); # Connectivity With File

print(data.read());

data.close(); # Close Connectivity

with open("./app2.txt") as file:

    print(file.readline(), end=""); # Read Only One Line At A Time

    print(file.readline(), end="");

    print(file.readlines());

with open("./app2.txt", "r") as file: # By Default Is R (Read)

    print(file.readlines()[:3]);

with open("./app3.txt", "r+") as file:

    print(file.read());

    file.write(" Release Imran Khan");

    file.seek(0); # Add Particular Value In Cursor

    print("After:",file.read()); # Then It Show Blank 

with open("./app4.txt", "w") as file: # If File Exist Then It Overwrite The Text

    file.write("Free "); # If File Not Exist Then It Will Create New File

with open("./app4.txt", "a") as file: # If File Not Exist Then It Will Create New File & Exist File Add Content

    file.write("Palestine");

with open("./app5.txt", "x") as file: # If File Not Exist Then It Will Create New File

    file.write("Pakistan Zindabad"); # # If File Exist Then Return Thorw Error

with open("./app4.txt", "rb+") as file: # Read, Binary Mode & Plus Means (All)

    print(file.read()); # Binary Format For Read Content

import pandas as pd;

df : pd.DataFrame = pd.read_csv("./data.csv");

print(df);

df : pd.DataFrame = pd.read_excel("./data.xlsx");

print(df);

import matplotlib.pyplot as plt;

import matplotlib.image as mpimg;

img = mpimg.imread("./PM.jpeg");

print(plt.imshow(img));

from typing import List;

import PyPDF2;

def read_pdf(file_path: str) -> List[str]:

    with open(file_path, "rb") as file:

        reader: PyPDF2.PdfReader = PyPDF2.PdfReader(file);

        text_content: List[str] = [page.extract_text() for page in reader.pages];
        
        return text_content;

pages: list[str] = read_pdf("./mypdf.pdf");

print(pages);

class StudentCard():

    def __init__(self, roll_no: int, name: str, age: int) -> None:

        if age < 18 or age > 60:
            
            raise StudentAgeError("Your Are Not Eligible For This Program!"); # Raise Throw Error In Python

        self.roll_no = roll_no;

        self.name = name;

        self.age = age;

class StudentAgeError(Exception): # Custom Error Class

    pass;

student = StudentCard(44, "Ahmed", 23);

print(student.name, student.roll_no, student.age);

# student2 = StudentCard(34, "Bilal", 17);

# ============= Return Error("Your Are Not Eligible For This Program!"); ============= #