person = ("Rahul", 25, 5.9)
print("Age:", person[1])


#GEMINI versions ჯერ არ ვიცი
#1
person = ("Rahul", 25, 5.9)
Age = person[1]
# ეს დაბეჭდავს - Age=25
print(f"{Age=}")

#2
person = ("Rahul", 25, 5.9)
labels = ("Name", "Age", "Height")
# ვიღებთ მეორე ლეიბლს და მეორე მნიშვნელობას
print(f"{labels[1]}: {person[1]}")

#3
from collections import namedtuple
# ვქმნით შაბლონს
User = namedtuple('User', ['Name', 'Age', 'Height'])
person = User("Rahul", 25, 5.9)
# ახლა შეგვიძლია ასე დავბეჭდოთ:
print(f"Age: {person.Age}")