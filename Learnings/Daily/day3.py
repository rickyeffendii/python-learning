# Day 3 - Collections

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits.append("fig") # adds "fig" to the end of the list
fruits.insert(2, "grape") # inserts "grape" at index 2 (between "banana" and "cherry")
fruits.remove("date") # removes "date" from the list
popped_fruit = fruits.pop(3) # removes and returns the fruit at index 3 (which is "elderberry")

nums = [0, 1, 2, 3, 4, 5]
print(nums[0]) # prints the first element of the list (1)
print(nums[-1]) # prints the last element of the list (5)
print(nums[1:4]) # prints a slice of the list from index 1 to index 3 (not including index 4), which is [2, 3, 4]
print(nums[:3]) # prints a slice of the list from the beginning to index 2 (not including index 3), which is [1, 2, 3]
print(nums[2:]) # prints a slice of the list from index 2 to the
print(nums[::2]) # prints every second element of the list, which is [1, 3, 5]
print(nums[::-1]) # prints the list in reverse order, which is [5, 4, 3, 2, 1]

point = (2, 3) # a tuple representing a point in 2D space
print(point[0], point[1]) # prints the x-coordinate and y-coordinate of the point (2, 3)

# point[0] = 4 # this will raise a TypeError because tuples are immutable and cannot be modified after they are created

def get_min_max(numbers):
    if not numbers: # check if the list is empty
        return None, None
    return min(numbers), max(numbers)

low, high = get_min_max([3, 1, 4, 1, 5, 9])

a, b = 1, 2 # this is called unpacking, it assigns the value 1 to a and the value 2 to b
b, a = a, b # this is a common way to swap the values of two variables without using a temporary variable
print(a, b) # this will print 2 1, because the values of a and b have been swapped

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person["name"]) # prints the value associated with the key "name", which is "Alice"
print(person.get("age")) # prints the value associated with the key "age", which is 30
print(person.get("country", "Unknown")) # tries to get the value associated with the key

person["country"] = "USA" # adds a new key-value pair to the dictionary
person["email"] = "alice@example.com" # adds another key-value pair
person["age"] = 31 # updates the value associated with the key "age" to 31

for key, value in person.items(): # iterates over the key-value pairs in the dictionary
    print(f"{key}: {value}") # prints each key and its corresponding value
    
if 'email' in person:
    print("Email is present in the dictionary.")
    
squares = {x: x**2 for x in range(10)} # dictionary comprehension, this creates a dictionary where the keys are numbers from 0 to 9 and the values are the squares of those numbers

registered_usernames = {"alice", "bob", "charlie"} # a set of registered usernames
new_username = input("Enter a new username: ")

if new_username in registered_usernames:
    print("This username is already taken. Please choose a different one.")
else:    
    registered_usernames.add(new_username) # adds the new username to the set of registered usernames
    print("Username registered successfully.")