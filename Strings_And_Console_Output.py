# Set the variable brian on line 3!
#from test import datetime
brian = "Hello life"

# Assign your variables below, each on its own line!
caesar = "Graham"
praline = "John"
viking = "Teresa"


# Put your variables above this line
print (caesar)
print (praline)
print (viking)

# The string below is broken. Fix it using the escape backslash!
print ('This isn\'t flying, this is falling with style!')


#The string "PYTHON" has six characters,
#numbered 0 to 5, as shown below:

#+---+---+---+---+---+---+
#| P | Y | T | H | O | N |
#+---+---+---+---+---+---+
#  0   1   2   3   4   5

#So if you wanted "Y", you could just type
#"PYTHON"[1] (always start counting from 0!)

fifth_letter = "MONTY"[4]

print (fifth_letter)

#String methods
parrot = "Norwegian Blue"
print (len(parrot))

# Write your code below, starting on line 3!

my_string = "Someday we will find it."
print (len(my_string))
print (my_string.upper())

print('Alpha')
print("Bravo")
print(str(3))

print(len("Charlie"))
print("Delta".upper())
print("Echo".lower())

print ("Foxtrot")

g = "Golf"
h = "Hotel"
print ("%s, %s" % (g, h))

#The datetime Library
from datetime import datetime

now = datetime.now()
print (now)
print (now.year)
print (now.month)
print (now.day)

print ('%s/%s/%s' % (now.month, now.day, now.year))
print ('%s:%s:%s' % (now.hour, now.minute, now.second))
print ('%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second))