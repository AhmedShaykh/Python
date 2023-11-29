value: str = "Imran Khan";

print(value);

print(type(value));

print(id(value));

print([i for i in dir(value) if "__" not in i]);

value: int = 4;

print(value);

print(type(value));

print(id(value));

value: float = 5.8;

print(value);

print(type(value));

print(id(value));

value: bool = True;

print(value);

print(type(value));

print(id(value));

value: list[str] = ["Pakistan", "Nertherlands", "Canada"];

print(value);

print(type(value));

print(id(value));

value: tuple[int] = [7, 8, 6];

print(value);

print(type(value));

print(id(value));

value: tuple[str, int, float] = ["Ahmed", 7, 4.4];

print(value);

print(type(value));

print(id(value));

value: any = [];

print(value);

print(type(value));

print(id(value));