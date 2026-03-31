#classes are user defined blueprint or prototype
#sum, multiplication, addition, constant
#methods, class variables, instance variables, constructor etc
#objects from your classes

class calculator1:
    num = 100

    def getData(self):
        print("I am now executing as method in class")

obj = calculator1()  #syntax to create objects in phyton
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

print('-------------------------------------------')

class LegalConsultation:
    # 1. Class Variable (Same for everyone)
    hourly_rate = 50

    # 2. Constructor (Initializes the object)
    def __init__(self, name, hours):
        self.client_name = name        # Instance Variable
        self.consultation_hours = hours # Instance Variable
        print(f"New consultation registered for: {self.client_name}")

    # 3. Method to calculate the total fee
    def calculate_fee(self):
        # We use 'return' to give the result back to the program
        return self.consultation_hours * LegalConsultation.hourly_rate

# --- Creating Objects (Instances) ---

# 4. Create the first object 'obj1'
obj1 = LegalConsultation("Keti", 3)

# 5. Call the method and store the result in a variable
total_fee = obj1.calculate_fee()
print(f"Fee for {obj1.client_name}: {total_fee} GEL")

# 6. Create the second object 'obj2'
obj2 = LegalConsultation("Nino", 5)
print(f"Fee for {obj2.client_name}: {obj2.calculate_fee()} GEL")