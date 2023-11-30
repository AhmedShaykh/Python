from typing import Dict, Set, Union, List, TypedDict, Tuple, Any;
import pprint;
import json;

data : Dict[str,str] = { "fName": "Ahmed", "mName": "Saleem", "lName": "Shaikh" };

print(data);

print(type(data));

pprint.pprint(data); # Print In Sequence

data: Set = {1, 1, 4, 5, 4, 7};

print(data); # Set Type Return Unique Value In Order & Not Apply Indexing

Key = Union[int, str];

Value = Union[int, str, list, dict, tuple, set];

data : Dict[Key, Value] = { 
                            "fName": "Ahmed", 
                            "mName": "Saleem", 
                            "lName": "Shaikh",
                            100: "Pakistan",
                            "Array": [1, 2, 3],
                            "Obj": {1, 2, 3},
                            "Fun": (1, 2, 3),
                            "Oop": {"A": 1, "B": 2}
                        };

pprint.pprint(data);

print(data["fName"]);

print(data[100]);

print(data["Obj"]);

print(data["Oop"]);

print(data["Oop"]["A"]);

data: Set = {1, 1, 4, 5, 4, 7};

print(data);

listData: List[int] = list(data);

print(listData);

Key = Union[int, str];

Value = Union[int, str, list, dict, tuple, set];

data : Dict[Key, Value] = {};

data["Country"] = "Nertherlands";

data["Message"] = "Free Palenstine";

data["Learning Language"] = "Python";

pprint.pprint(data);

print([i for i in dir(data) if "__" not in i]); # Check Set Data Types Methods & Attributes

print(data.get("Pakistan", "Not Available"));

print(data.get("Message", "Not Available"));

Key = Union[int, str];

Value = Union[int, str, list, dict, tuple, set];

data : Dict[Key, Value] = { 
                            "Country": "Nertherlands",
                            "Message": "Free Palenstine",
                            "Learning Language":"Python"
                        };

for value in data:

    pprint.pprint(value);

print(data.keys()); # Keys

print(data.values()); # Values

print(data.items()); # All Items In Dictionary

for val in data.keys():

    print(val);

    print(f"{data[val]} \n");

for key, val in data.items():

    print(key, val);

pprint.pprint({ key:val for key,val in data.items() }); # Comprehension List

pprint.pprint({ val:key for key,val in data.items() }); # Shuffle

a : int = 7;

b : int = 9;

a, b = b, a; # Shuffle

print(a,b);

Key = Union[int, str];

Value = Union[int, str, list, dict, tuple, set];

data : Dict[Key, Value] = { 
                            "Country": "Nertherlands",
                            "Message": "Free Palenstine",
                            "Learning Language":"Python"
                        };

print(data);

data.clear();

print(data);

data : Dict[Key, Value] = { 
                            "Country": "Nertherlands",
                            "Message": "Free Palenstine",
                            "Learning Language":"Python"
                        };

pprint.pprint(data);

val: str = data.pop("Country");

print(val); # Pop Remove Particular Item

pprint.pprint(data);

data : Dict[Key, Value] = { 
                            "Country": "Nertherlands",
                            "Message": "Free Palenstine",
                            "Learning Language":"Python"
                        };

pprint.pprint(data);

val: str = data.popitem();

print(val); # PopItem Remove Last Item

pprint.pprint(data);

data : Dict[Key, Value] = { 
                            "Country": "Nertherlands",
                            "Message": "Free Palenstine",
                            "Learning Language":"Python"
                        };

pprint.pprint(data);

val: str = data.get("Message", "No Message Available");

print(val);

pprint.pprint(data);

data : Dict[Key, Value] = { 
                            "Country": "Nertherlands",
                            "Message": "Free Palenstine",
                            "Learning Language":"Python"
                        };

pprint.pprint(data);

val: str = data.setdefault("Learning Language", "TypeScript"); # Return Same Value Not Update

print(val);

val2: str = data.setdefault("LLM", "Empty Value"); # Add New Value In Object Not Return Error Message

print(val2);

pprint.pprint(data);

Key = Union[int, str];

Value = Union[int, str, list, dict, tuple, set];

data : Dict[str,str] = { 
                        "fName": "Ahmed", 
                        "mName": "Saleem", 
                        "lName": "Shaikh",
                        "Country": "Pakistan"
                    };

data2 : Dict[Key, Value] = { 
                            "Country": "Nertherlands",
                            "Message": "Free Palenstine",
                            "Learning Language":"Python"
                        };

data.update(data2);

pprint.pprint(data);

print(f"{data.keys()} \n");

print(f"{data.values()} \n");

pprint.pprint(f"{data.items()}");

Key = Union[int, str];

Value = Union[int, str, list, dict, tuple, set];

keys : List[str] = ["fName", "mName", "lName", "Country"];

data : Dict[Key,Value] = {};

data = data.fromkeys(keys);

print(data);

values : List[str] = ["Ahmed", "Saleem", "Shaikh", "Pakistan"];

data = data.fromkeys(keys, values); # Values Add In All Keys Items

pprint.pprint(data);

import pandas as pd;

data : Dict[str, list[Any]] = {
                                "No": [1, 2, 3], 
                                "Company": ["Apple", "SpaceX", "Google"],
                                "Net Worth": ["$2.72 Trillion", "$150 Billion", "$1585.58 Billion"],
                            };

result: pd.DataFrame = pd.DataFrame(data);

print(result);

alien: Dict[Any, Any] = {"XPosition": 0, "YPosition": 25, "Speed": "Medium"};

print(f"""Original Position: {alien["XPosition"]}""");

if alien["Speed"] == "Slow":

    increment = 1;

elif alien["Speed"] == "Medium":

    increment = 2;

else:

    increment = 3;

alien["XPosition"] += increment;

print(f"""New Position: {alien["XPosition"]}""");

alien: Dict[Any, Any] = {"XPosition": 0, "YPosition": 25, "Speed": "Medium"};

alien["Speed"] = "Fast";

if alien["Speed"] == "Slow":

    increment = 1;

elif alien["Speed"] == "Medium":

    increment = 2;

else:

    increment = 3;

alien["XPosition"] += increment;

print(f"""New Position: {alien["XPosition"]}""");

data : Dict[str,str] = { 
                        "fName": "Ahmed", 
                        "mName": "Saleem", 
                        "lName": "Shaikh",
                        "fName": "AHM X" # Key Is Always Unique Put In Multiple Same Value But It Support Last Value
                    };

print(data);

val = data["fName"].upper();

print(f"My Name Is {val}");

favLanguages : Dict[str,str] = { 
                                "Jen": "JavaScript",
                                "Sarah": "Python",
                                "Edward": "Solidity",
                                "Phil": "TypeScript",
                            };

friends: List[str] = ["Phil", "Sarah"];

for name in favLanguages.keys():

    print(f"Hi {name}");

    if name in friends:

        languages = favLanguages[name];

        print(f"{name.upper()}, I See You Love {languages}");

print("Erin" not in favLanguages.keys());

print(favLanguages.keys());

check: str = "Ahmed" in """My Name Is Ahmed. I'm Full Stack Developer""";

print(check); # In Method Check Value In Word As Word

alien: Dict[str, int] = {"Color": "Green", "Points": 5};

alien2: Dict[str, int] = {"Color": "Yellow", "Points": 10};

alien3: Dict[str, int] = {"Color": "Red", "Points": 15};

aliens: List[Dict[str, int]] = [alien, alien2, alien3];

print(aliens);

for alienData in aliens:

    print(alienData);

aliens: List[Dict[str, int]] = [];

print(aliens);

for alienNumber in range(30):

    alien = {"Color": "Black", "Points": 15, "Speed": "Fast"};
    
    aliens.append(alien);

pprint.pprint(aliens);

pprint.pprint(aliens[:5]);

for alien in aliens[:5]:

    if alien["Color"] == "Black":

        alien["Color"] = "Blue";

        alien["Speed"] = "Medium";

        alien["Points"] = 10;

pprint.pprint(aliens[:10]);

for alien in aliens[0:9]:

    if alien["Color"] == "Black":

        alien["Color"] = "Blue";

        alien["Speed"] = "Medium";

        alien["Points"] = 10;

    elif alien["Color"] == "Blue":

        alien["Color"] = "White";

        alien["Speed"] = "Slow";

        alien["Points"] = 5;

pprint.pprint(aliens);

Key = Union[int, str];

Value = Union[int, str, list, dict, tuple, set];

data : Dict[Key, Value] = { 
                            "Country": "Nertherlands",
                            "Message": "Free Palenstine",
                            "Learning Language":"Python"
                        };

print(data);

dataJSON = json.dumps(data, indent = 4); # Indent Add Space In JSON

print(type(dataJSON));

print(dataJSON);

dataJSON = json.dumps(data, indent = 12);

print(dataJSON);

dataType = TypedDict(
    "dataType",
    {
        "a": int,
        "b": int
    }
);

myDataType = TypedDict(
    "myDataType", {
        "fname": str,
        "name": str,
        "id": Union[str, int],
        "abc": List[int],
        "xyz": Set[int],
        "efg": Tuple,
        "cde": dataType
    }
);

data: myDataType = {
    "fname": "Ahmed Saleem",
    "name": "Ahmed",
    "id": 44,
    "abc": [1, 2, 3],
    "xyz": {1, 2, 3},
    "efg": (1, 2, 3),
    "cde": {"a": 1, "b": 2}
};

pprint.pprint(data);

print(data["cde"]["b"]);

print(data["cde"]);

print(data["id"]);