# #solution 1


class Person:
  def __init__(abc, name, age):
    abc.name = name
    abc.age = age





p1 = Person("mohamad", 36)
p2 = Person("yazdan" , 23)







print(p1.name)
print(p1.age)
print(p2.name)


#Solution 2

class Person:
  pass



p1 = Person()
p2 = Person()

p1.name = "mohamad"
p2.name = "yazdan"
p1.age = 25
p2.age = 20

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

###################################################################################################################################


cars = ["Ford", "Volvo", "BMW"]

print(cars)

for x in cars:
  print(x)
