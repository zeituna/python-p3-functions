#!/usr/bin/env python3

# 1. No arguments, prints greeting
def greet_programmer():
    print("Hello, programmer!")

# 2. One argument, prints greeting
def greet(name):
    print(f"Hello, {name}!")

# 3. One argument with default value
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# 4. Returns sum of two numbers
def add(num1, num2):
    return num1 + num2

# 5. Returns half of a number
def halve(number):
    return number / 2