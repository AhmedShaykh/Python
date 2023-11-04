def piaic() -> None: # Default Function

    print("Learning Generative AI");

    print("Artificial Intelligence");

piaic();

def addNumbers(num1: int , num2: int) -> int:

    return num1 + num2;

print(addNumbers(7,20));

num = lambda num1, num2 : num1 + num2;

print(num(12, 20));

from typing import Callable, List;

add: Callable[[int, int], int] = lambda x, y: x + y;

result = add(10, 20);

print(result);

data: List[int] = [1,2,3,4,5,6,7,8,9,10];

data = list(map(lambda x: x ** 2, data));

print(data);

data: List[int] = [1,2,3,4,5,6,7,8,9,10];

data = list(filter(lambda x: x % 2 == 0, data));

print(data);

data: List[int] = filter(lambda x: x % 2 == 0, range(1,101));

print(next(data)); # Next Perform Single Iteration Code By Code

print(next(data));

print(list(data));

def myRange(start: int , end: int,step: int = 1):

    for i in range(start, end + 1, step):

        yield i; # Identity

fun = myRange(1,10);

print(list(fun));

from collections.abc import Iterator;

def myRange(start: int , end: int,step: int = 1) -> Iterator[int]:

    for i in range(start, end + 1, step):

        yield i;

fun = myRange(1,10);

print(next(fun));

print(next(fun));

print(list(fun));

print(type(fun));

def add(*nums):

    print(nums, type(nums));

    total = 0;

    for n in nums:

        total += n;

    return total;

add(1,2,3,3,5,6);

from typing import Tuple;

def greet(*names: Tuple[str, ...]) -> None:

    for name in names:

        print("Hello", name);

greet("Martin", "Sam", "Steve", "Robert", "Sabrina", "Andrew");

from typing import Dict;

def greet(**xyz: Dict[str,str]) -> None:

    print(xyz);

greet(c = "Pakistan", a = "China", b = "Russia");

def xyz(**args):

    print(args, type(args));

xyz(a = 7, b = 20, c = 30, x = 1, y = 2, name = "AHM X");

def myfunc(a: int, b: int, *abc: Tuple[int, ...], **xyz:Dict[str,int]):

    print(a, b, abc, xyz);

myfunc(1, 2, 7, 9, 9, 9, c = 20, d = 30, x = 100);

from typing import Callable;

def myDecorator(func: Callable[[int], None])-> Callable[[], None]:

    def wrapper(num1: int) -> None:

        print("Something Is Happening Before The Function Is Called.");

        func(num1);

        print("Something Is Happening After The Function Is Called.");
    
    return wrapper;

@myDecorator

def sayHello(num1: int):

    print(num1);

sayHello(100);

def factorial(x: int) -> int:

    if x == 1:

        return 1;
    
    else:

        return (x * factorial(x-1));

num = 5;

print("The Factorial Of", num, "Is", factorial(num));

from typing import Callable;

def outerFunc(x: int) -> Callable[[int], int]:

    def innerFunc(y: int) -> int:

        return x + y;

    return innerFunc;

closure = outerFunc(10);

print(closure(5));