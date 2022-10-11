#Using the Work done expression W=f*d

while True:
  force = int(input("Enter the force value:  "))
  if force > 0:
    break
while True:
  distance = int(input("Enter the distance value:  "))
  if distance > 0:
    break
print("The Workdone is", force * distance)

#REFACTORED code

def input_positive_integer(prompt):
  while True:
    input_value = int(input(prompt))
    if input_value > 0:
      return input_value

force = input_positive_integer("Enter the force value:  ")
distance = input_positive_integer("Enter the distance:  ")
print("The Workdone is", force * distance, "J")
