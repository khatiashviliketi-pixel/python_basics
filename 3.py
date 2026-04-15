
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("First fruit:",fruits[0])
print("Last fruit:",fruits[-1])

print("Fruits from index 1 to 2:", fruits[1:3])



#Gemini versions (არ ვიცი ჯერ ესენი)
#1
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

start = 1
end = 3 # გვახსოვს, რომ 3-ს არ თვლის, ამიტომ რეალურად 1-დან 2-მდეა

# f-string-ში პირდაპირ ვიყენებთ ცვლადებს
print(f"Fruits from index {start} to {end-1}: {fruits[start:end]}")

#------------------------------------------------------------------------------
#2
def print_slice(my_list, a, b):
    # ეს ფუნქცია თავისით ააწყობს წინადადებას
    print(f"Fruits from index {a} to {b-1}: {my_list[a:b]}")

# ახლა უბრალოდ ვიძახებთ ფუნქციას სხვადასხვა ციფრებით
print_slice(fruits, 1, 3)
