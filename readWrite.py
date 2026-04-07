
file = open('test.txt')
# Read all the contents of file
# read n number of characters by passing parameter

#print(file.read(5))

# read one single line at a time readLine()

print(file.readline())
print(file.readline())

file.close()

# Print  line by line using readLine method

# GEMINI
#მეთოდი,რას აკეთებს?,კურსორის მოქმედება
#read(n),კითხულობს n სიმბოლოს.,ჩერდება n სიმბოლოს მერე.
#read(),კითხულობს მთლიან ფაილს.,გადადის ფაილის სულ ბოლოში.
#readline(),კითხულობს ხაზს ბოლომდე.,გადადის შემდეგი ხაზის დასაწყისში.
#readlines(),კითხულობს ყველა ხაზს და აბრუნებს სიას (List).,გადადის ფაილის ბოლოში.