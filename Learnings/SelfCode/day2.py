# FizzBuzz

n = input("Please input a number: ")

while n.isdigit() == False:
    print("This is not a valid number. Please try again.")
    n = input("Please input a number: ")

n = int(n)
for i in range(1, n+1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
doubles = [x * 2 for x in range(1, 11)]
odds = [x for x in range(1, 30) if x % 2 == 1]
words = ["apple", "banana", "cherry", "date", "elderberry", "kiwi", "lemon", "mango", "nectarine", "orange"]
lengths = [len(word) for word in words]
uppercase = [word.upper() for word in words if len(word) > 4]
celcius = [0, 10, 20, 30, 40, 100]
fahrenheit = [x * 9/5 + 32 for x in celcius]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mixed = [x if x % 2 == 1 else "even" for x in numbers]
words = ["hi", "yo"]
flattened_word = [letter for word in words for letter in word] # this is a nested list comprehension, it will flatten the list of words into a list of letters