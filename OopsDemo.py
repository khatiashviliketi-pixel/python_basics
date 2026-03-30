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

print('-------------------------------------------')
def say_hello(): # ეს არავის არ ეკუთვნის, "თავისუფალია"
    print("Hello")

say_hello() # იმუშავებს `obj.`-ის გარეშე.

print('-------------------------------------------')

#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you created object

class calculator:
    num = 100  #class variables
    #default constructor
    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b
        print('I am called automatically when object is created')

    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstnumber + self.secondnumber + calculator.num


obj = calculator(2,3)
obj.getData()
print(obj.summation())

obj1 = calculator(4,5)
obj1.getData()
print(obj1.summation())