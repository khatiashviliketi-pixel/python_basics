#classes are user defined blueprint or prototype
#sum, multiplication, addition, constant
#methods, class variables, instance variables, constructor etc
#objects from your classes

class calculator:
    num = 100

    def getData(self):
        print("I am now executing as method in class")

obj = calculator()  #syntax to create objects in phyton
obj.getData()
print(obj.num)


def say_hello(): # ეს არავის არ ეკუთვნის, "თავისუფალია"
    print("Hello")

say_hello() # იმუშავებს `obj.`-ის გარეშე.