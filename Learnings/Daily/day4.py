# Day 4 - Error Handling
import os
from pathlib import Path

# while True:
#     try:
#         x = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print("That's not a valid number. Please try again.")
        
        
try:
    raise Exception("This is an error message.", "Additional info")
except Exception as e:
    print(e.args) # this will print the arguments passed to the exception, in this case it will print the error message and the additional info as a tuple
    print(e) # this will print the string representation of the exception, which is the error message by default
    
    x, y = e.args # this will unpack the arguments into two variables, x will be the error message and y will be the additional info
    print(f"Error message: {x}")
    
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid integer. Please try again.")
            
# age = get_integer("Please enter your age: ")
# print(f"You entered: {age}")

def read_first_line(filename):
    file = None
    try:
        file_path = Path(__file__).parent / "numbers.txt"
        file = open(file_path, 'r')
        first_line = file.readline()
        number = int(first_line.strip()) # remove any leading/trailing whitespace
        print(f"The first line of the file is: {number}")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except ValueError:
        print("The first line of the file is not a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if file:
            file.close() # this will ensure that the file is closed even if an error occurs
            print("File has been closed.")
            
# read_first_line("numbers.txt")

def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__} instead.")
    if age < 0 or age > 150:
        raise ValueError(f"Age must be between 0 and 150, got {age} instead.")
    print(f"Age has been set to {age}.")
    
class InvalidContactError(Exception):
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"Invalid Contact - {field}: {message}")
        
def add_contact(name, email):
    if not name or not isinstance(name, str):
        raise InvalidContactError("Name", "Name must be a non-empty string.")
    if "@" not in email:
        raise InvalidContactError("Email", "Email must contain an '@' symbol.")
    print(f"Contact added: {name} with email {email}.")
    
try:
    set_age("thirty")
except TypeError as e:
    print(e)
    
try:
    set_age(200)
except ValueError as e:
    print(e)
    
try:
    add_contact("", "valid@example.com")
except InvalidContactError as e:
    print(e)
    print(f"Error field: {e.field}")