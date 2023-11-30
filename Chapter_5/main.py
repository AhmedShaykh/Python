if True:
    print("Pakistan Zindabad");

else:
    print("Hello World!");

print("Hello World!") if False else print("Pakistan Zindabad");

if False:

    print("True Block");

elif False:

    print("Elif Logic 1");

elif True:

    print("Elif Logic 2");

elif False:

    print("Elif Logic 3");

else:

    print("Final Else Block");

print("Learning Python 3.12");

from typing import Union;

per : Union[int, float] = float(input("Enter Your Percentage:"));

grade :Union[str, None] = None;

if per >= 80:
    grade = "A+";
elif per >= 70:
    grade = "A";
elif per >= 60:
    grade = "B";
elif per >= 50:
    grade = "C";
elif per >= 40:
    grade = "D";
elif per >= 33:
    grade = "E";
else:
    grade = "Fail";

print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");

from typing import Union, Optional;

per : Union[int, float] = 32;

grade :Optional[str] = None; # Optional Default Is None

if per >= 80:
    grade = "A+";
elif per >= 70:
    grade = "A";
elif per >= 60:
    grade = "B";
elif per >= 50:
    grade = "C";
elif per >= 40:
    grade = "D";
elif per >= 33:
    grade = "E";
else:
    grade = "Fail";

print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");

from typing import Union;

per : Union[int, float] = float(input("Enter Your Percentage:"));

grade :Union[str, None] = None;

if (per >= 0) and (per < 33):
    grade = "Fail";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
elif (per >= 33) and (per < 40):
    grade = "E";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
elif (per >= 40) and (per < 50):
    grade = "D";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
elif (per >= 50) and (per < 60):
    grade = "C";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
elif (per >= 60) and (per < 70) :
    grade = "B";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
elif (per >= 70) and (per < 80) :
    grade = "A";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
elif (per >=80 )and (per < 100):
    grade = "A+";
    print(f"Dear Student Your Percentage Is {per} Now Your Calculated Grade Is: {grade}");
else:
    print("Error 404");

from typing import Union;

PerType = Union[float, int];

percentages : list[PerType] = [88, 99.9, 50, 51,65,70];

grades : list[str] = [];

for per in percentages:

    grade : str = "";

    if (per >= 0) and (per < 33):
        grade = "Fail";
    elif (per >= 33) and (per < 40):
        grade = "E";
    elif (per >= 40) and (per < 50):
        grade = "D";
    elif (per >= 50) and (per < 60):
        grade = "C";
    elif (per >= 60) and (per <70) :
        grade = "B";
    elif (per >= 70) and (per <80) :
        grade = "A";
    elif (per >=80) and (per <= 100):
        grade = "A+";

    grades.append(grade);

print(percentages);

print(grades);

cars : list[str] = ["tesla", "bugatti", "lamborghini", "ferrari"];

print([i.upper() if i == "bugatti" else i.title() for i in cars]);

cars : list[str] = ["tesla", "bugatti", "Civic", "lamborghini", "ferrari"];

for car in cars:

    if car != "Civic":

        print(car.upper());
    
    else:

        print(car.title());

pizzaAvailable : list[str] = ["Mushrooms", "Olives", "Green Peppers", "Extra Cheese", "Pepperoni"];

pizzas : list[str] = ["Mushrooms", "Tikka", "Extra Cheese"]; # Input Pizza

for pizza in pizzas:

    if pizza in pizzaAvailable:

        print(f"Adding {pizza} Pizza.");

    else:

        print(f"Sorry, We Don't Have {pizza}.");

print("\nFinished Making Your Pizza!");

userName : str = input("Enter Your Username:");

passwrod : str = input("Enter Your Password:");

if userName and passwrod:

    print("Sent OTP On Your Registered Number");

    otp : str = input("Please Enter OTP:");

    if otp == "123":

        print(f"Welcome {userName}");

    else:

        print("Incorrect Your OTP");

else:

    print("Invalid User Or Password");