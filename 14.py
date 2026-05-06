
lineCount = 0
with open('file1.txt', 'r') as file:
    for line in file.readlines():  #for _ in file.readlines(): line როცა არ გვჭირდება სიტყვა ესეც წერენო
        lineCount = lineCount + 1
    print("Total number of lines:", lineCount)



#იგივე ლოგიკაა რაც "loops" ფაილში მაქვს ნასწავლი
#summation = 0
#for j in range(1, 6):
#    summation = summation + j
#print(summation)


