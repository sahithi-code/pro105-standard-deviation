import math
import csv

with open("data.csv",newline='') as f :
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0

    for x in data :
        total+=int(x)
    mean = total/n
    return(mean)

#squaring and get value

squared_listed = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squared_listed.append(a)

#sum
sum = 0
for i in squared_listed:
    sum = sum+i

#for n-1
resullt=sum/(len(data)-1)

standard_deviation= math.sqrt(resullt)

print("the standard deviation is : ",str(standard_deviation))
