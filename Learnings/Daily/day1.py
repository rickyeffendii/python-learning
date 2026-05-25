# Day 1 - First Python Code
int1 = 8 / 5  # always returns a float
int2 = 8 // 5 # floor division, returns the integer part of the division
int3 = 2 ** 3 # exponentiation, returns 2 raised to the power of 3
int4 = round(22/7, 2) # rounds the result to 2 decimal places

string1 = 'Hello, World!' # a string variable
string2 = "Python is great!" # another string variable
string3 = 'It\'s a nice day!' # using escape character to include a single quote
string4 = "She said, \"Hello!\"" # using escape character to include double quotes
string5 = """This is a multi-line string.
It can span multiple lines.""" # a multi-line string
string6 = "First line.\nSecond line." # using \n to create a new line
string7 = r"C:\Users\Name\Documents" # using raw string to ignore escape characters
string8 = f"The value of int1 is {int1}" # using f-string to include variable values in a string
string9 = "The value of int2 is {}".format(int2) # using format method to include variable values in a string
string10 = "The value of int3 is %d" % int3 # using old-style string formatting
string11 = "The value of int4 is {:.2f}".format(int4) # using format method to format a float to 2 decimal places
string12 = 3 * "Hello! " + "How are you?" # repeating a string 3 times
string13 = "Hello" "World" # concatenating two strings
char1 = string1[0] # accessing the first character of string1
char2 = string1[-1] # accessing the last character of string1
# char3 = string1[20] # this will raise an IndexError because string1 has only 13 characters (index 0 to 12)
char4 = string1[2:5] # slicing from the 2nd character to the 5th character (not including the 5th character)
char5 = string1[7:] # slicing from the 7th character to the end of string1
char6 = string1[:5] # slicing from the beginning to the 5th character

list1 = ["red", "green", "blue"] # a list of strings
list2 = [1, 2, 3, 4, 5] # a list of integers
list3 = [1, "two", 3.0, [4, 5]] # a list with mixed data types
list4 = list1
id(list1) == id(list4) # True, because list4 is just another reference to the same list object as list1
list4.append("yellow") # this will modify the original list1 as well, because list4 is referencing the same list object
# print(list1) # this will show the modified list1
# print(string12)

# Fibonacci sequence using a loop
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(f"number {i+1} is {a}\n")
        a, b = b, a + b

fibonacci(10) # prints the first 10 numbers in the Fibonacci sequence

name = "Ricky"
age = 28
height = 1.68
isLearning = True

print(f"My name is {name}, my age is {age}, my height is {height}, and am I learning Python? {isLearning}.")

# userName = input("Enter your username: ")
# password = input("Enter your password: ")
# print(f"Your username is {userName} and your password is {password}.")

print(type(name))
print(type(age))
print(type(height))
print(type(isLearning))

message = "python is fun"
print(message.upper()) # converts the string to uppercase
print(message.capitalize()) # converts the first character to uppercase and the rest to lowercase
print(message.split()) # splits the string into a list of words
print(message.replace("fun", "awesome")) # replaces "fun" with "awesome"