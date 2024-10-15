# 1. Basic Arithmetic Operations
a = 10
b = 5

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print(addition, subtraction, multiplication, division)

# 2. String Manipulation
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)

# Reversing a string
reversed_name = name[::-1]
print(reversed_name)

# 3. Finding Factorial (Using Recursion)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# 4. List Comprehension
squares = [x**2 for x in range(10)]
print(squares)

# 5. Fibonacci Sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 6. Dictionary Example
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

# Accessing dictionary values
print(phonebook["Alice"])

# 7. File Handling: Writing and reading a file
with open("example.txt", "w") as file:
    file.write("This is an example text.")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 8. Random Number Generation
import random

random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

# 9. Class and Object
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

my_dog = Dog("Rex", "German Shepherd")
my_dog.bark()  # Output: Rex is barking!

# 10. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")
