# string = ტექსტი ბრჭყალებში

str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"


print(str1)
print(str[1])     #a

print(str[0:5])   # if you want substring in Python

print(str+str1)   # concatenation

print(str3 in str)    # substring check

print("Shetty" in str)  # ეს მე მოვიგონე

var = str.split(".")
print(var)

print(str.split("."))   # ეს მე მოვიგონე, მაგრამ არაა სასურველიო ჯემინიმ

print(var[0])
print(var[1])

print("***********************************************")

str4 = " Great "
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())

