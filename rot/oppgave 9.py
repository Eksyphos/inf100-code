from random import randrange
people =[
    {"name":"Arild", "age":9},
    {"name":"Ingvild", "age":16},
    {"name":"Aashild", "age":86},
]
i=randrange(3)
print(i)
name = people[i]["name"]
age = people[i]["age"]
print(f"{name} is the winner. They are {age} years old.")