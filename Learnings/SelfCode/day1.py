# Introduction

name = input("Fill in your name: ")
year = input("Fill in your birth year: ")
languages = input("Fill in the programming languages you know (separated by commas): ")
age = 2026 - int(year)
print(f"Hello, {name}! You are {age} years old!")
print(f"You know the following programming languages: {languages.split(",")}")