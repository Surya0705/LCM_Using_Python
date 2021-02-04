a = int(input("Enter First Number: ")) # Taking the First Number as Input from the User.
b = int(input("Enter Second Number: ")) # Taking the Second Number as Input from the User.

if a > b: # Putting an if Condition that What to do if 'a' is Greater than 'b'.
    c = a # Telling the Program that let 'c' be equal to 'a' if 'a' is Greater than 'b'.
else: # Putting an Else Condition so that Program knows what to do if 'a' is Smaller than 'b'.
    c = b # Telling the Program that let 'c' be equal to 'b' if 'b' is Greater than 'a'.
d = c # Equalizing 'd' to 'c'. You will come to know later why I did so.

while True: # Putting a While loop so that the Program keeps on Trying until it gets the Result.
    if c % a == 0 and c % b == 0: # Giving it instructions that what formula needs to be implemented.
        print(f"The LCM of {a} and {b} is {c}.") # Printing the Output. Note that I hav used f string here.
        break # Breaking the Program otherwise the Output will keep on Printing forever.
    else: # Putting an Else condition so that Program knows what to do if the 'if condition' gets wrong.
        c = c + d # Now here comes why in line 8 I did 'd = c'. That's because for instance I took 5 and 7 so if 7 is not the LCM so the Program adds input value that might also be 7 and it is a kind of Tables going on. So now 'c' gets a new value and the Program repeats itself because it is in While Loop.