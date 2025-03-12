

# Conditional Flow : Spacing and indentation is very important. 
#Syntax:  
# Comparison operators : >    <     >=     <=    ==      != 
# if condition:
#    action1
# else:
#    action2
# if - else
if 10>20:
    print("Is greater")
else:
    print("Is not greater.")

## Modulo Operator : '%'
# This will output the remainder. 
print(22%7)      # Remainder is '1'. 


# Odd : Even Challenge.
number = int(input("Enter the number to check : "))
if number % 2 == 0:
    print("This is an Even Number")
else:
    print("This is an ODD number.")


# Nested Conditional :
# using if, elif and else together. 

# Syntax:
#if condition1:
#   do A
#elif condition2:
#   do B
#else:
#   do C

if 10 < 20:                       # condition
 print("Action 1 ")               # Action. 
 if 20 > 11:
    print("Action 1:1 ")
 elif 10 > 2:                     # Condition, We can have multiple 'elif' in between 'if' and  'else'.
    print("Action : 2:0 ")
 else:
    print("Last nested...")
else:
 print("Action 2 ")


