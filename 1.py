greeting = "Welcome to Python Programming"
name = "Rahul!"
print(greeting)
print(greeting + ", " + name)



# CHATGPT versions
#1
greeting = "Welcome to Python Programming"
name = "Rahul!"

print(greeting)
print(f"{greeting}, {name}")

#----------------------------------------------------------------------------------------
#2
greeting = "Welcome to Python Programming"
name = "Rahul!"

print(greeting)
print("{}, {}".format(greeting, name))

#----------------------------------------------------------------------------------------
#3
greeting = "Welcome to Python Programming"

print(greeting)

greeting = greeting + ", Rahul!"
print(greeting)

#-----------------------------------------------------------------------------------------
#4
greeting = "Welcome to Python Programming"
name = "Rahul!"

print(greeting)
print(greeting, name)
# აქ მძიმე არ დაიწერა

#print("Age:", 20)      # მუშაობს
#print("Age: " + 20)    # ❌ შეცდომა
# + მხოლოდ string-ებზე მუშაობს, ხოლო , ნებისმიერ ტიპზე.