a=10
if (a == 10):
    print("wow")
# a= 1/0  
"""
#four types of variable

*** name
*** type       python care about type and name 
*** value
* memeory address = python Don't care about it.
 type dictatestwo things
      what kind of date varaible can hold.
      what opeartions can be done on that data
Names:
**alpha numeraic
**can nnot strat with a digit
**can have undercsores
**no spaces

ALL_CAPS is used to indicate constants
= 3 asisgnment opeartor
== equality operator

#caesar's cypher
#attack at dawn
#cvvcem cv fcyp

literal means unnamed constant. = a value or number or string hardcoded into the program

PEMDAS
P = Parenthesis
E = exponent
M = Multiplication
D = Division
A = Addition
S = subtraction

"""

hungry = True
if hungry:
     print("Let's go eat")
     
# if you use boolean varaible and later on adds statement which depnds on them it became flgs
# hungry is a boolean variable (True/False)
# used in decisisons later
# booleans varible are called "flags"

a=900000000001
print(a)

name= ""
name += "Joe" #concatenated (appending) (adding)
name += ", Jack"
print(name)

# data type dictates what kind of datae can be stored
# and the operations that can be done
# for string, addtion and multiplication
# + (concat) and * (multiple concats)
# numeric types + - * / ** exponent // floor division  % modulus

"""
5 ** 2   25
5/2      2.5
5//2     2     floor division rounds down
5%2      1       remainder
8 % 4    0
"""
pennies = 9801
dollars = pennies //100
cents = pennies % 100
print("%10d %2f" % (dollars, cents))

story = """ I went to
walmart to get eggs """
print(story)

ounces = 100
pounds = ounces // 16
ounces = ounces % 16
print(pounds, ounces)

ounces = 100
pounds = ounces / 16
print(pounds)

s="1\n2\t3"
print(s)
s = "Hello\b\b\b\bi"
print(s)

s = "c:\\newdir"
print(s)
s= "I love \"eggs\""
print(s)

s= 'I love "eggs"'
print(s)

purchase = 90
taxrate = 0.075 
 #Variable names in caps represent values that should not be change

tax = purchase * taxrate
print(tax)

SPEED_OF_LIGHT = 2.998e8 #(constant ..it will never change)

#Caesar's Cypher
msg ="A"
val =ord(msg) #ordinal value MENAS ORD GETS THE ORDINAL (ASCII) val of charcter
print(val)
val +=2
msg2 = chr(val) # chr converts the ordinal value to a character
print(msg2)
