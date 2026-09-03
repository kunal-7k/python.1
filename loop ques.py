i=1
while i<11 :
    print(i)
    i=i+1

i=10
while i>0 :
    print(i)
    i=i-1    


for i in range (1,20):
    if i%2==0:
        print(f"even number: {i}")
 
 
i=2
while i<21:
    if i%2==0:
        print(f"even number: {i}")
    i=i+1

i=1
sum=0
while i<=10:
    sum=sum+i
    i=i+1
    
print(sum)
sum=0
for i in range (1,11):
    
    sum=sum+i
    
    
print(sum)    
multiply=1
for i in range(5,0,-1):
    multiply=multiply*i
print(multiply)    

for i in range (1,21):
    if i%2==1:
        print(f"odd number{i}")
        
        
sum=0
for i in range (2,21,2):
    sum=sum+i
print(sum)    


numbers = [12, 45, 7, 89, 34, 56]
largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print(largest)
    
            