# Day 2 - Control Flow
x = int(input("Enter a number: "))
if x > 0:
    print("The number is positive.")
elif x < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

words = ["apple", "banana", "cherry"]
for word in words:
    print(word, len(word))

users = {"Alice": "Active", "Bob": "Inactive", "Charlie": "Active", "David": "Inactive"}
# active_users = [user for user, status in users.items() if status == "Active"]
active_users = {}
for user, status in users.items():
    if status == "Active":
        active_users[user] = status

users2 = {"Eve": "Active", "Frank": "Inactive", "Grace": "Active", "Heidi": "Inactive"}
for user, status in users2.copy().items():
    if status == "Inactive":
        del users2[user]

for i in range(2, 10, 2): # this will print even numbers from 2 to 8
    print(i)

# for i in range(100, 1, -2): # this will print odd numbers from 99 down to 3
#     print(i)

list1 = ['apple', 'banana', 'cherry']
for i in range(len(list1)):
    print(f"Index: {i}, Value: {list1[i]}")

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")
    
for n in range(2, 15):
    for divisor in range(2, n):
        if n % divisor == 0:
            print(f"{n} equals {divisor} * {n // divisor}")
            break
    print(f"{n} is a prime number")