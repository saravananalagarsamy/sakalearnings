import time

max = int(input("Enter the maximum number: "))
#print numbers from 0 to max-1
for i in range(max):
    print(i)

for i in range(1,max):
    print(i) 

for i in range(1, max + 1):
    print(i)

#with increment of 2
for i in range(1, max + 1, 2):
    print(i)

name = str(input("Enter your name: "))
for letter in name:
    print(letter, end=' ')    


for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Blastoff!")