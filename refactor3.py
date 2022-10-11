# USING TERNARY OPERATOR

to_check = int(input("Enter a whole number :"))
msg = "Even" if to_check%2 == 0 else "Odd"
print("The number you entered is", msg, "number")


# USING USUAL IF-ELSE

to_check = int(input("Enter a whole number :"))
msg = ""
if(to_check%2 == 0):
  msg = "Even"
else:
  msg = "Odd"
print("The number you entered is", msg, "number")
