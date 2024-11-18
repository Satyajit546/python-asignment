# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Nnut69dv48gUbgme-6WllpZgwpjvUzo8
"""



"""1.Explain the key features of python that make it a popular choice for programming

Python’s popularity stems from a combination of powerful features that make it versatile, accessible, and efficient. Here are some key features that contribute to its widespread use:
1. Easy to Read, Write, and Learn
•	Python has a simple and clean syntax, making it beginner-friendly and readable. This lowers the learning curve for new programmers and speeds up development time.
2. Interpreted Language
•	Python is an interpreted language, meaning code is executed line-by-line, which makes debugging easier and code testing faster. This feature is ideal for interactive development and iterative workflows.
3. Dynamic Typing
•	Python uses dynamic typing, allowing variables to change types at runtime. This flexibility can make programming quicker and easier for certain applications, though it can introduce runtime errors if not carefully managed.
4. Extensive Standard Library and Third-Party Packages
•	Python’s standard library supports many programming tasks (e.g., file I/O, system calls, and web development). Additionally, it has a vast ecosystem of third-party libraries through the Python Package Index (PyPI) for specialized tasks like data analysis, machine learning, web development, and more.
5. Cross-Platform Compatibility
•	Python is available on multiple platforms, including Windows, macOS, and Linux, and Python code can run on any operating system with minimal changes. This portability is highly valued by developers.
6. Support for Multiple Paradigms
•	Python supports various programming paradigms, including procedural, object-oriented, and functional programming, allowing developers to choose the style that best fits the problem.
7. Strong Community and Documentation
•	Python has a large, active community that contributes to extensive documentation, tutorials, and forums. This makes troubleshooting easier and provides support for both new and experienced developers.
8. Integration and Extensibility
•	Python can easily integrate with other languages like C, C++, and Java, allowing for performance optimizations and interoperability. For example, libraries like Python help combine Python with C code, enhancing performance in computationally heavy applications.
9. Ideal for Rapid Prototyping and Development
•	With features like dynamic typing and a vast library, Python enables quick prototyping and efficient project iterations, ideal for startups, data science projects, and research applications.
10. Suitability for Automation and Scripting
•	Python is commonly used for scripting and automating tasks, with simple syntax that makes it accessible for non-programmers and professionals in various fields looking to automate workflows.
11. Excellent Tooling for Data Science and Machine Learning
•	Python’s powerful libraries for data science (e.g., Pandas, NumPy, SciPy) and machine learning (e.g., TensorFlow, PyTorch, Scikit-Learn) have made it the language of choice for these domains, offering high performance, visualization tools, and robust data processing capabilities.

# **2. Describe the role of predifined keywords in python and provide examples of how they are used in a program**

1. Control Flow Keywords
•	Control flow keywords help in defining the flow of execution within a program, such as conditional statements and loops.
•	Examples: if, else, elif, for, while, break, continue
"""

for i in range(5): # example of control flow keywords
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

"""2. Function Definition and Return Keywords
•	Keywords like def and return are used to define functions and return values.
•	Examples: def, return

"""

def x (name): # Example of function definition and return
    return f"Hello, {name}!"

print(x("satyajit"))

"""5. Boolean Keywords
•	These keywords are used to represent boolean values and logical operations.
•	Examples: True, False, and, or, not

"""

# Example of boolean keywords
is_raining = False
is_cold = True

if not is_raining and is_cold:
    print("It's cold but not raining.")

"""4. Exception Handling Keywords
•	Python uses specific keywords to manage exceptions, allowing the program to handle errors gracefully.
•	Examples: try, except, finally, raise

"""

# Example of exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
finally:
    print("Execution finished.")

"""6. Variable Declaration and Scope Keywords
•	Python uses global and nonlocal keywords to specify the scope of variables in functions and nested functions.
•	Examples: global, nonlocal

"""

# Example of global and nonlocal
x = 10

def outer():
    x = 5

    def inner():
        nonlocal x  # Refers to x in the outer function
        x += 5
        print("Inner x:", x)

    inner()
    print("Outer x:", x)

outer()

"""7. Miscellaneous Keywords
•	Some keywords serve other unique functions within Python’s syntax.
•	Examples: pass, lambda, yield, with

"""

# Example of miscellaneous keywords
# 'pass' acts as a placeholder
for i in range(3):
    if i == 1:
        pass  # No action taken
    else:
        print(i)

# 'lambda' creates anonymous functions
double = lambda x: x * 2
print(double(4))

# 'with' simplifies resource management
with open("file.txt", "w") as file:
    file.write("Hello, world!")

"""# 3.Compare and contrast mutable and imutable objects in python with exmples

1. Definition
•	Mutable Objects: Objects that can be modified after creation. Changes can be made to the original object without creating a new instance in memory.
•	Immutable Objects: Objects that cannot be changed after creation. Any "modification" will create a new instance in memory rather than changing the original.
2. Common Mutable and Immutable Types

  Mutable Types-
list, dict, set

  Immutable Types-
	int, float, str, tuple, frozenset
3. Behavior with Examples
Example of Mutable Object: list
•	Lists in Python are mutable, meaning we can change their content by modifying elements, appending new items, or removing items.
"""

# Mutable example with a list
my_list = [1, 2, 3]
print("Original list:", my_list)

# Modify an element
my_list[0] = 10
print("Modified list:", my_list)

# Append a new element
my_list.append(4)
print("Appended list:", my_list)

"""Example of Immutable Object: str
•	Strings in Python are immutable, meaning any operation that alters a string creates a new string object rather than modifying the original.

"""

# Immutable example with a string
my_str = "hello"
print("Original string:", my_str)

# Attempting to modify the string by "changing" it
new_str = my_str.replace("h", "H")
print("Modified string:", new_str)
print("Original string remains:", my_str)

"""6. Passing to Functions
•	Mutable Objects: If a mutable object is passed to a function, modifications within the function will affect the original object.
•	Immutable Objects: If an immutable object is passed to a function, the original object remains unchanged; any changes create a new object.

"""

# Mutable example: modifying a list inside a function
def modify_list(lst):
    lst.append(100)

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)

# Immutable example: modifying a string inside a function
def modify_string(s):
    s += " world"

greeting = "hello"
modify_string(greeting)
print(greeting)

"""# 4.Discuss the different types of operators in python and provide examples of how they are used

Python provides a variety of operators that enable you to perform computations, comparisons, and other operations on data. Here’s a rundown of the main types of operators in Python, along with examples of how they’re used.
1. Arithmetic Operators
•	Used to perform basic mathematical operations such as addition, subtraction, multiplication, etc.

Operator	Description	Example
+	Addition	3 + 2 = 5
-	Subtraction	3 - 2 = 1
*	Multiplication	3 * 2 = 6
/	Division	     3 / 2 = 1.5

%	Modulus (remainder)	3 % 2 = 1

**	Exponentiation	3 ** 2 = 9

//	Floor Division	3 // 2 = 1
"""

# Example of arithmetic operators
x, y = 10, 3
print("Addition:", x + y)
print("Floor Division:", x // y)

"""2. Comparison Operators
•	Used to compare two values. They return True or False.
Operator	Description	Example
==	Equal to	3 == 3 = True

!=	Not equal to	3 != 2 = True

>	Greater than	3 > 2 = True

<	Less than	3 < 2 = False

>=	Greater than or equal to	3 >= 3 = True

<=	Less than or equal to	3 <= 2 = False

"""

# Example of comparison operators
x, y = 5, 10
print("Is x equal to y?", x == y)
print("Is x less than y?", x < y)

"""3. Assignment Operators
•	Used to assign values to variables. Python also supports compound assignment operators, which combine arithmetic and assignment.
Operator	Description	Example
=	Assign	x = 5

+=	Add and assign	x += 3 (same as x = x + 3)

-=	Subtract and assign	x -= 3

*=	Multiply and assign	x *= 3

/=	Divide and assign	x /= 3

%=	Modulus and assign	x %= 3

**=	Exponent and assign	x **= 3

//=	Floor division and assign	x //= 3

"""

# Example of assignment operators
x = 5
x += 2  # Equivalent to x = x + 2
print("x after += 2:", x)

"""4. Logical Operators
•	Used to combine multiple conditions. They return a boolean value (True or False).

Operator	      Description	                                Example

and	       True if both conditions are true	            (x > 5 and y < 10)


or	    True if at least one condition is true   	       (x > 5 or y < 10)

not 	Inverts the result; True if the condition is false	not      (x > 5)



"""

# Example of logical operators
x, y = 5, 10
print("x > 2 and y < 15:", x > 2 and y < 15)
print("not x < 5:", not (x < 5))

"""5. Bitwise Operators
•	Used to perform operations on binary representations of numbers. Often used in low-level programming.

Operator  	Description	           Example

&	          Bitwise AND	            x & y

`	`	        Bitwise OR

^	         Bitwise XOR	                x ^ y

~	           Bitwise NOT	               ~x

<<	         Bitwise left shift	        x << 2

>>	        Bitwise right shift	         x >> 2

"""

# Example of bitwise operators
x, y = 6, 3  # In binary: x = 110, y = 011
print("Bitwise AND:", x & y)
print("Bitwise OR:", x | y)

"""6. Membership Operators
•	Used to check if a value exists within a sequence (e.g., strings, lists, tuples).


Operator	    Description	          Example


in	     True if value is in the sequence	"a" in "apple"


not in	True if value is not in the sequence	"b" not in "apple"

"""

# Example of membership operators
my_list = [1, 2, 3]
print("Is 2 in my_list?", 2 in my_list)
print("Is 4 not in my_list?", 4 not in my_list)

"""7. Identity Operators
•	Used to compare the memory locations of two objects.

Operator	       Description	                          Example

is	True if both are the same object	                        x is y


is not	True if both are not the same object	            x is not y

"""

# Example of identity operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)
print("x is z:", x is z)

"""# 5.Explain the concept of type casting in python with examples

Type casting in Python (also known as type conversion) is the process of converting a variable from one data type to another. This is especially useful when you need to interact with different data types in a program. Python supports two main types of type casting:
1.	Implicit Type Casting
2.	Explicit Type Casting
Let's explore each with examples.
1. Implicit Type Casting
In implicit type casting, Python automatically converts a variable from one type to another when it’s safe to do so. This happens mostly with numeric data types (like int to float), where there’s no risk of losing information.

Example of Implicit Type Casting
"""

# Implicit type casting from int to float
x = 5       # x is an integer
y = 2.5     # y is a float

result = x + y  # Python converts x to a float to perform the addition
print(result)
print(type(result))

## 1.	String to Integer Conversion
age = "25"         # age is a string
age = int(age)     # Convert age to an integer
print(age + 5)
print(type(age))

##2.	Float to Integer Conversion
price = 99.99      # price is a float
price = int(price) # Convert price to an integer
print(price)

##3.	Integer to String Conversion
score = 85          # score is an integer
score_str = str(score)   # Convert score to a string
print("Your score is " + score_str)

## 4.	String to Float Conversion
height = "5.9"       # height is a string
height = float(height) # Convert height to a float
print(height + 0.1)

##5.	List to Tuple Conversion
numbers = [1, 2, 3]    # numbers is a list
numbers_tuple = tuple(numbers)  # Convert to a tuple
print(numbers_tuple)
print(type(numbers_tuple))

#6.	String to List Conversion
word = "hello"
letters = list(word)    # Convert to a list of characters
print(letters)

"""# 6 How do conditional statement work in python illustrate with examples

In Python, conditional statements allow you to make decisions in your code by checking specific conditions and executing code blocks based on whether these conditions are True or False. The main conditional statements in Python are if, elif, and else. Here’s a breakdown of each, along with examples.
1. if Statement
•	The if statement evaluates a condition, and if the condition is True, the code block within the if statement runs.

2. if...else Statement
•	The else statement is used to specify a block of code that will run if the if condition is False.
"""

age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

"""3. if...elif...else Statement
•	The elif (short for "else if") allows you to check multiple conditions sequentially. If the first condition is False, Python checks the next elif condition, and so on. If all conditions are False, the else block runs.
Syntax:
python
Copy code
if condition1:
    ## Code to execute if condition1 is True

elif condition2:
    ## Code to execute if condition1 is False and condition2 is True

else:
     ##Code to execute if both condition1 and condition2 are False


"""

marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

"""4. Nested if Statements
•	You can place an if statement inside another if statement to check multiple levels of conditions. This is known as nesting, and it is useful when a condition depends on another condition.

"""

age = 20
nationality = "US"

if nationality == "US":
    if age >= 18:
        print("You are eligible to vote in the india.")
    else:
        print("You are not eligible to vote in the india.")
else:
    print("You are not eligible to vote in the india.")

"""5. Using Logical Operators in Conditions"""

#Example with and:
age = 25
income = 40000

if age > 18 and income >= 30000:
    print("Eligible for loan.")
else:
    print("Not eligible for loan.")

#Example with or:
age = 17
parent_permission = True

if age >= 18 or parent_permission:
    print("Allowed to attend event.")
else:
    print("Not allowed to attend event.")

#Example with not:
is_raining = False

if not is_raining:
    print("You can go outside.")

"""# 7.Describe the different types of loop in python and thier use caseswith examples

1. for Loop
•	The for loop in Python is primarily used to iterate over a sequence (like a list, tuple, string, or range) or any iterable object. With each iteration, it assigns an element from the sequence to a variable, allowing you to work with each element directly.

•	Use Case: When you know the number of iterations in advance, such as when you’re working with a collection of items or a predefined range.


Syntax:

for variable in sequence:
    # Code to execute
"""

#Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Example 2: Using for with range()
for i in range(5):
    print(i)

#Example 3: Iterating over a string
word = "hello"
for letter in word:
    print(letter)

"""2. while Loop
•	The while loop repeats a block of code as long as a specified condition is True. With each iteration, it checks the condition, and if it remains True, it executes the loop’s code block again.
•	Use Case: When you don’t know the number of iterations in advance and want the loop to continue until a specific condition is no longer met.

Syntax:

while condition:
    # Code to execute

"""

#Example 1: Using a counter with while

counter = 0
while counter < 5:
    print("Counter:", counter)
    counter += 1

#Example 2: Repeated user input until a condition is met

password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

"""3. Nested Loops
•	Both for and while loops can be nested within each other. This is useful for working with multi-dimensional data, such as matrices or nested lists.
•	Use Case: When you need to iterate over items within each item of another iterable (e.g., iterating over rows and columns in a matrix).

"""

#Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

"""4. Control Statements in Loops
•	break: Terminates the loop entirely and moves to the next line after the loop.
•	continue: Skips the current iteration and continues with the next one.
•	else: Used with loops to specify a block of code that runs when the loop completes normally (i.e., not interrupted by break).

"""

#Example of break:

for i in range(5):
    if i == 3:
        break
    print(i)

#Example of continue:

for i in range(5):
    if i == 2:
        continue
    print(i)

#Example of else:

for i in range(5):
    print(i)
else:
    print("Loop completed!")