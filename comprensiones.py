#List Comprehension instead of For Loop

numbers = [1,2,3,4,5,6,7,8]
odd_numbers = []
for item in numbers:
  if item % 2 == 1:
    odd_numbers.append(item)
print(odd_numbers)

#Outcome will be [1,3,5,7]

numbers = [1,2,3,4,5,6,7,8]
odd_numbers = [item for item in numbers if item % 2 == 1]
print (odd_numbers)