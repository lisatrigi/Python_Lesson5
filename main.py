# loops - for

fruits = ["apple", "banana", "watermelon", "strawberry"]

for fruit in fruits:
    print(fruit)

fjala = "Kimik"

for shkronja in fjala:
        print(shkronja)

# in range

for number in range(1,11):
    if number == 5:
         break
    print(number)

for number in range(1,11):
    if number == 5:
         continue
    print(number)

numbers = [1,2,3,4,5,6,7,8,9] #minichallenge

total_sum = 0

for num in numbers:
    if num %2 ==0:
         total_sum = total_sum + num
    
    print("Shuma totale e numrave cift eshte: ",total_sum)
