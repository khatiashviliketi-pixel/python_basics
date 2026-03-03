
values = [1, 2, "rahul", 4, 5]
# List is a data type that allows multiple values and can be different data types

print(values[0]) # 1

print(values[3]) # 4
print(values[-1]) #5
print(values[1:3]) # 2 rahul
print(values[1:2])
print(values[:3])
print(values[0:3])
print(values[2:])
print(values[:])

values.insert(3, "shetty")   # [1, 2, 'rahul', 'shetty', 4, 5]
print(values)

values.append("end")   # [1, 2, 'rahul', 'shetty', 4, 5, 'end']
print(values)

values[2]= "RAHUL"    #updating

del values[0]
print(values)



# Tuple - Same as list data type but immutable
val = (1, 2, "rahul", 4.5)
print(val[1])

 # val[2] = "RAHUL"    # impossible
print(val)




#Dictionary
dic = {"a": 2, 4:"bcd", "c": "hello World"}
print(dic[4])
print(dic["c"])


#  list [], Tuple () არ იცვლება, Dictionary {key:value}]

#
dict = {}
dict["firstname"] = "Rahul"
dict["lastname"] = "Shetty"
dict["gender"] = "male"

print(dict)
print(dict['lastname'])

