class Teacher:

    def __init__(self, teacherId : int, teacherName : str) -> None: # Method / Constructor (__Init__)

        self.name : str = teacherName; # Attribute

        self.teacherId : int  = teacherId;

        self.organizationName: str = "PIAIC";

    def quarter(self, quarter : int ) -> None: # Method

        print(f"This Is Quarter {quarter}");
    
    def teaching(self, subject : str ) -> None:

        print(f"{self.name} Is Teaching {subject}...!");

obj1 : Teacher = Teacher(1, "Sir Zia Khan");

obj2 : Teacher = Teacher(2, "Sir Qasim");

print(f"Name: {obj1.name}, ID: {obj1.teacherId} & Organiztion: {obj1.organizationName} \n");

print(f"Name: {obj2.name}, ID: {obj2.teacherId} & Organiztion: {obj2.organizationName} \n");

obj1.teaching("BlockChain")

obj2.teaching("Generative AI")

print(dir(obj1));

class Teacher:

    counter : int = 0; # Variable

    classTiming : str = "8 PM";

    def __init__(self, teacherId : int, teacherName : str) -> None:

        self.name : str = teacherName;

        self.teacherId : int  = teacherId;

        self.organizationName: str = "PIAIC";
    
        Teacher.counter += 1;

    def quarter(self, quarter : int ) -> None:

        print(f"This Is Quarter {quarter}");
    
    def teaching(self, subject : str ) -> None:

        print(f"{self.name} Is Teaching {subject}...!");

    def details(self) -> None:

        information : str = f"""
        Teacher Name Is {self.name}
        Class Timing is {Teacher.classTiming}
        """;
        
        print(information);

print(Teacher.counter);

obj1 : Teacher = Teacher(1, "Sir Zia Khan"); # Create New Object Then Increase The Value Of Counter

print(obj1.counter); # And Also Run The Object Increase The Value Of Counter

print(obj1.counter);

print(Teacher.counter);

obj2 : Teacher = Teacher(2, "Sir Qasim");

print(obj1.counter);

print(obj2.counter);

print(Teacher.counter);

obj1.details();

print(id(obj2));