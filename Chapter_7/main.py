from typing import Dict, List;

name : str = input("What Is Your Name?: ");

print(type(name));

print(f"My Name Is {name}!");

flag : bool = True;

number : int = 0;

while flag:

    print(f"No. {number}");

    number += 1;

    if number == 10:

        break;

data : List[Dict[str,str]] = [];

flag : bool = True;

while flag:

    print("Write Quit Or Exit To Stop This Program");

    name : str = input("Enter Your Name: ");

    eduction: str = input("Enter Your Education: ");

    if name in ["Exit","Quit","Close","Stop"] or eduction in ["exit","quit","close","stop"]:

        flag = False

        break;

    data.append(
                { "name":name,
                  "education": eduction }
                );

print(data);

for i in range(1, 11):

    if i == 5:

        print(f"Number {i}");

        continue;
    
    print(i);

if True:

    pass; # Escape The Logic Go To Next Line

print("Free Palestine");

prompt: str = "Enter Value:";

active = True;

while active:

    message = input(prompt);

    if message == "Quit":

        active = False;
    
    else:

        print(message);

unConfirmedUsers: list[str] = ["Bilal", "Yaseen", "Usman"];

confirmedUsers: list[str] = [];

while unConfirmedUsers:

    currentUser = unConfirmedUsers.pop();

    print(f"Verifying user: {currentUser.upper()}");

    confirmedUsers.append(currentUser);

print("\nThe Following Users Have Been Confirmed:");

for confirmedUser in confirmedUsers:

    print(confirmedUser);