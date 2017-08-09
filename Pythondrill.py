# -*- coding: cp1252 -*-
    
# 1 Assign an integer to a variable
x = 5
print x

# 2 Assign a string to a variable
name = "joaquin"
print name
print name.capitalize()

# 3 Assign a float to a variable
print float(7)

# 4 Use the print function and .format() notation to print out the variable you assigned
print '{} {}'.format('one', 'two')

# 5 Use each of these operators +, - , * , / , +=, ­= , %

def letsAdd(x,y):
    addition = x + y
    return addition
print letsAdd(4, 7)

def letSub(x,y):
    subtract = x + y
    return subtract
print letSub(5, 2)

def letsMult(x,y):
    multiply = x * y
    return multiply
print letsMult(5, 2)

def letDiv(x,y):
    divide = x / y
    return divide
print letDiv(10, 2)

x = 5
x += 2
print (x)

x = 5
x -= 2
print (x)

def letPer(x,y):
    percent = x % y
    return percent
print letPer(20, 3)


# 6 Use of logical operators: and, or, not
a = True
b = False

print( a and b)

print( a or b)

print (not (a and b))

# 7 Use of conditional statements: if, elif, else

x = 3

if x == 5:
    print 'x = 5'

elif x == 4:
    print 'x = 4'

else:
    print 'x does not equal 4 or 5'

# 8 Use of a while loop

counter = 0

while counter < 10:
    print counter
    counter +=2

# 9 Use of a for loop

for counter in range(0,10):
    print counter

# 10 Create a list and iterate through that list using a for loop to print each item out on a new line
euro_soccer_list = ["FC Barcelona",
                    "Real Madrid",
                    "Manchester United",
                    "Juventus",
                    "PSG",]
for team in euro_soccer_list:
    print "Top Euro soccer team: " + team
# 11 Create a tuple and iterate through it using a for loop to print each item out on a new line

for name in ('Luis','Juan','Antonio'):
     print("Hello",name)


# 12 Define a function that returns a string variable

def square(x):
    y = x * x
    return y

toSquare = 11
result = square(toSquare)

# 13 Call the function you defined above and print the result to the shell
print "The result of " + str(toSquare) + " squared is " + str(result)

