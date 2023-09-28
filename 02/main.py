class person :

    name = "yazdan"
    age = 23


person1 = person
person2 = person
person1.name = "yazdan"
print(person1.name)
person2.name= "mohammad"

del person2.age


print(person2.name)
print(person2.age)
print(person1.name)

# class person :
#     pass
#
# person1 = person



