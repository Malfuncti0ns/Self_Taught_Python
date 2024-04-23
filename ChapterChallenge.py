# 1. Print three different strings.

print("This is my first string")
print("This is my second string")
print("This is my third string")

# 2. Write a program that prints a message if a variable is less than 10, and different message if the variable is greater than or equal to 10.

number = input("Please input a number: ")

if int(number) < 10:
    print("This number is less than 10!")
else:
    print("This number is bigger than 10")
    
# 3. Write a program that prints a message if a variable is less than or equal to 10, another message if the variable is greater than 10 
# but less than or equal to 25, and another message if the variable is greater than 25.

number = input("Please input a number: ")
if int(number) < 10:
    print("This number is less than 10!")
elif int(number) >10 or int(number) <=25:
    print("This number is between 10 and 25")
else:
    print("This number is greater than 25!")

# 4. Create a program that divides two variables and prints the remainder.

x = input("Please enter the first number: ")
y = input("Please enter the second number: ")
sum = (float(x) / float(y)) 
# Made a float because we want the remainder which can be a decimal
print(sum)

# 5. Create a program that takes two variables, divides them, and prints the quotient.

x = input("Please enter the first number: ")
y = input("Please enter the second number: ")
sum = (int(x) // int(y)) 
print(sum)

# 6. Write a program with a variable age assigned to an integer that prints different strings depending on what integer age is.

age = 20

if age < 18:
    print("You can't drink, get back on the soft drink!")
else:
    print("Over 18? The pubs are not closed, it's time to get on the beers")