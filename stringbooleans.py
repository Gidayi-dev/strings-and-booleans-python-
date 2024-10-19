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
