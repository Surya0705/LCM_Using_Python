import math # Importing the Math Module.

a = int(input("Enter First Number: ")) # Taking first Number as the Input from User.
b = int(input("Enter Second Number: ")) # Taking Second Number as the Input from User.

'''In the Line-8 I have used the lcm function from the module for finding the LCM.
I have Even Used f string to Print results effectively.'''
print(f"The LCM of {a} and {b} is {math.lcm(a, b)}.") # Printing the Output.