#loops

#while loop
count = 0

while(count < 3):
    print('the count is: ', count)
    count += 1
    print('goodbye')

#for loop

for var in list(range(5)):
    print("iteration: ", var)

print('\n')

for letter in 'python 57': #traversal of a string sequence
    print('curr letter: ', letter)

print('\n')

fruits = ['banana', 'apple', 'mango']
for fruit in fruits: #traversal of list sequence
    print('current fruits -> ', fruit)
