from typing import List;

records: List[str] = ["Revealed", "Spinnin", "Armada", "Monstercat", "STMPD"];

for record in records: # Indentation
    
    print(f"{record} \n");

print("Is Top EDM Records Label");

from typing import Tuple;

data_base : List[Tuple[str,str]] = [("Ahmed","456"), ("Bilal","628")];

for row in data_base:
    
    user, number = row;

    print(user, number);

names: List[str] = ["Ahmed", "Saleem", "Shaikh"];

for name in names:

    print(name);

    break;

print("Ahmed Shaykh");

print([i ** 2 for i in range(1,11)]);

letters: Tuple[str, ...] = ("A","B","C");

print(letters[0]);

data: tuple[str, int, float] = ("Ahmed", 56, 7.8);

print(data);

from typing import Any;

data: Tuple[Any] = ("A", [1,2,3], True);

print(data[1]);

data[1].append(20); # Because It's List

print(data);