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