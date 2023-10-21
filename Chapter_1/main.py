print("Hello Python 3.12");

message = "Learning Generative AI!";

print(message);

print(type(message));

print(id(message)); # Physical Address

print(dir(message)); # Methods & Attributes

print([i for i in dir(message) if "__" not in i]); # All Methods & Attributes