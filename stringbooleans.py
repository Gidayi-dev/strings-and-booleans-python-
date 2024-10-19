#Check String
#Use it in an if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
#You Python - Slicing Strings
#In Python, slicing strings is a powerful way to access a portion of a string, allowing you to create new strings from parts of the original.
text = "Hello, World!"
slice1 = text[0:5]  # 'Hello'

#The upper() method returns the string in upper case
a = "Understanding python"
print(a.upper())

#The lower() method returns the string in lower case
a = "Understanding python"
print(a.lower())

#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
#The strip() method removes any whitespace from the beginning or the end
a = "Understanding python"
print(a.strip())

#The replace() method replaces a string with another string
a = "Understanding python"
print(a.replace("Y", "J"))

#The split() method splits the string into substrings if it finds instances of the separator
a = "Understanding, split string in python"
print(a.split(","))

#String Concatenation
#To concatenate, or combine, two strings you can use the + operator
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
#provides space between hello & world
print(c)

#what is an f -string in python An f-string in Python, short for "formatted string literal," is a way to embed expressions inside string literals using curly braces {}. It's a convenient way to construct strings that include variable values or expressions directly within the string. This feature was introduced in Python 3.6.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
#:.2f is a format specifier that means "format this number as a floating-point number with 2 decimal places." Thus, {price:.2f} converts the integer 59 to the string "59.00"
print(txt)

a = 5
b = 10
result = f"The sum of {a} and {b} is {a + b}."
print(result)  # Output: The sum of 5 and 10 is 15.

#Escape characters in Python are used to insert characters that are illegal or difficult to include directly in a string. They start with a backslash (\). Here are some commonly used escape characters and what they do
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#Python Booleans
a = 200
b = 40

if b > a:
    print("b is greater than a")
else:
    print("b is less than a")
    

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#You can create functions that returns a Boolean Value
def myFunction() :
      return True

print(myFunction())

def myFunction() :
      return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
#python operators
#Python divides the operators in the following groups:
#Arithmetic operators: Arithmetic operators perform mathematical operations like addition, subtraction, multiplication, and division.

a = 10
b = 5
result = a + b  # 15
#Assignment operators: Assignment operators are used to assign values to variables.
a = 10
a += 5  # a = a + 5, a is now 15

#Comparison operators: Comparison operators compare two values and return a boolean result
a == b  # False
a != b  # True
a >= b  # True

#Logical operators: Logical operators are used to combine conditional statements.
a > 0 and b > 0  # True
#Not (not): Reverses the result of the condition.
not(a > 0)  # False
a = [1, 2, 3]
b = a
a is b  # True


#Identity operators: dentity operators compare the memory location of two objects.
a = [1, 2, 3]
b = a
a is b  # True

b = [1, 2, 3]
a is not b  # True

#Membership operators:Membership operators test for membership in a sequence, such as strings, lists, or tuples.
1 in a  # True
b = [1, 2, 3]
a is not b  # True

#Bitwise operators: Bitwise operators perform operations on the binary representations of integers.
a = 5  # 0101
b = 3  # 0011
result = a & b  # 0001, which is 1

result = a << 1  # 1010, which is 10


print((6 + 3) - (6 + 3))