from numpy import random

x = random.randint(100) #generate random num from zero to 100
print(x)

x = random.rand() #returns random num between 0 and 1
print(x)

x = random.rand(5) #generates 5 random numbers using rand b/w 0 and 1
print(x)

x = random.randint(100, size=(5)) #generate rand arr of size 5 w/ elements b/w 0 & 100
print(x)

x = random.randint(100, size=(3,5)) #generate rand arr of 3 rows, 5 cols w/ elements b/w 0 & 100
print(x)

x = random.choice([3,5,7,9]) #will pick any number randomnly from this array
print(x)



