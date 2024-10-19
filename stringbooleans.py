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
