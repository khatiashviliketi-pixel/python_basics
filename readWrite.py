
file = open('test.txt')
# Read all the contents of file   print(file.read())
# read n number of characters by passing parameter
#print(file.read(5))

# read one single line at a time readLine()
# print(file.readline())
# print(file.readline())


# GEMINI
#მეთოდი,რას აკეთებს?,კურსორის მოქმედება
#read(n),კითხულობს n სიმბოლოს.,ჩერდება n სიმბოლოს მერე.
#read(),კითხულობს მთლიან ფაილს.,გადადის ფაილის სულ ბოლოში.
#readline(),კითხულობს ხაზს ბოლომდე.,გადადის შემდეგი ხაზის დასაწყისში.
#readlines(),კითხულობს ყველა ხაზს და აბრუნებს სიას (List).,გადადის ფაილის ბოლოში.


# Print  line by line using readLine method

# line = file.readline()
# while line != "":
#    print(line)
#    line = file.readline()


# values = [abc, bvdsf, "cat", dog, elephant

for line in file.readlines():
    print(line)


# მეთოდი,რას აკეთებს?,შედეგი
# read(),კითხულობს ყველაფერს ერთიანად.,ერთი გრძელი ტექსტი (String).
# readline(),კითხულობს მხოლოდ ერთ ხაზს.,ერთი ხაზი (String).
# readlines(),კითხულობს ყველა ხაზს და ყოფს.,ხაზების სია (List).



file.close()