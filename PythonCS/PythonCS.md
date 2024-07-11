# Python Cheat Sheet

## Table of Contents
1. [Basic Syntax](#basic-syntax)
2. [Data Types](#data-types)
3. [Variables](#variables)
4. [Operators](#operators)
5. [Control Flow](#control-flow)
6. [Functions](#functions)
7. [Data Structures](#data-structures)
8. [Object-Oriented Programming](#object-oriented-programming)
9. [Modules and Packages](#modules-and-packages)
10. [File Handling](#file-handling)
11. [Exception Handling](#exception-handling)
12. [List Comprehensions](#list-comprehensions)
13. [Lambda Functions](#lambda-functions)
14. [Built-in Functions](#built-in-functions)
15. [Standard Library Modules](#standard-library-modules)
16. [Type Hints](#type-hints)

## Basic Syntax

- Python uses indentation to define code blocks
- Comments start with `#` for single line, or `'''` for multi-line
- Statements typically end with a newline
- Use `\` for line continuation

```python
# This is a comment
print("Hello, World!")  # This is also a comment

'''
This is a
multi-line comment
'''

print("This is a very \
long line of code")
```

## Data Types

- Numbers: `int`, `float`, `complex`
- Strings: `str`
- Boolean: `bool`
- Sequence Types: `list`, `tuple`, `range`
- Mapping Type: `dict`
- Set Types: `set`, `frozenset`
- Binary Types: `bytes`, `bytearray`, `memoryview`
- None Type: `None`

```python
# Examples
x = 5  # int
y = 3.14  # float
z = 1 + 2j  # complex
name = "Alice"  # str
is_valid = True  # bool
my_list = [1, 2, 3]  # list
my_tuple = (1, 2, 3)  # tuple
my_range = range(6)  # range
my_dict = {"name": "Bob", "age": 25}  # dict
my_set = {1, 2, 3}  # set
my_frozenset = frozenset([1, 2, 3])  # frozenset
my_bytes = b"hello"  # bytes
my_bytearray = bytearray(5)  # bytearray
my_memoryview = memoryview(bytes(5))  # memoryview
my_none = None  # NoneType
```

## Variables

- Variables are created when you assign a value
- Can be reassigned to different types
- Multiple assignment is possible

```python
x = 5
y = "John"
x, y, z = 5, "John", 3.14
```

## Operators

### Arithmetic Operators
- `+` (addition)
- `-` (subtraction)
- `*` (multiplication)
- `/` (division)
- `%` (modulus)
- `**` (exponentiation)
- `//` (floor division)

### Comparison Operators
- `==` (equal)
- `!=` (not equal)
- `>` (greater than)
- `<` (less than)
- `>=` (greater than or equal to)
- `<=` (less than or equal to)

### Logical Operators
- `and`
- `or`
- `not`

### Identity Operators
- `is`
- `is not`

### Membership Operators
- `in`
- `not in`

### Bitwise Operators
- `&` (AND)
- `|` (OR)
- `^` (XOR)
- `~` (NOT)
- `<<` (left shift)
- `>>` (right shift)

## Control Flow

### If-Elif-Else
```python
if condition:
    # code block
elif another_condition:
    # code block
else:
    # code block
```

### For Loop
```python
for item in iterable:
    # code block

# With range
for i in range(5):
    # code block
```

### While Loop
```python
while condition:
    # code block
```

### Break, Continue, and Pass
```python
for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    if i == 8:
        break  # Exit the loop
    if i == 5:
        pass  # Do nothing
    print(i)
```

## Functions

```python
def function_name(param1, param2="default"):
    """Docstring describing the function"""
    # Function body
    return result

# Function call
result = function_name(arg1, arg2)

# Arbitrary arguments
def func(*args):
    for arg in args:
        print(arg)

# Keyword arguments
def func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

## Data Structures

### Lists
```python
my_list = [1, 2, 3]
my_list.append(4)  # Add an item
my_list.extend([5, 6])  # Add multiple items
item = my_list.pop()  # Remove and return last item
del my_list[0]  # Remove item at index
my_list.remove(3)  # Remove first occurrence of value
my_list.sort()  # Sort the list in-place
sorted_list = sorted(my_list)  # Return a new sorted list
```

### Tuples
```python
my_tuple = (1, 2, 3)
# Tuples are immutable
```

### Dictionaries
```python
my_dict = {"name": "Alice", "age": 30}
my_dict["city"] = "New York"  # Add or update
del my_dict["age"]  # Remove a key-value pair
keys = my_dict.keys()  # Get all keys
values = my_dict.values()  # Get all values
items = my_dict.items()  # Get all key-value pairs
```

### Sets
```python
my_set = {1, 2, 3}
my_set.add(4)  # Add an item
my_set.update([5, 6, 7])  # Add multiple items
my_set.remove(3)  # Remove an item (raises error if not found)
my_set.discard(3)  # Remove an item (no error if not found)
```

## Object-Oriented Programming

```python
class MyClass:
    class_variable = "I'm a class variable"

    def __init__(self, param):
        self.instance_variable = param

    def method(self):
        return "I'm a method"

    @classmethod
    def class_method(cls):
        return "I'm a class method"

    @staticmethod
    def static_method():
        return "I'm a static method"

# Creating an instance
obj = MyClass("I'm an instance variable")

# Inheritance
class ChildClass(MyClass):
    def __init__(self, param):
        super().__init__(param)
```

## Modules and Packages

```python
# Importing a module
import module_name

# Importing specific items from a module
from module_name import function_name, ClassName

# Importing with an alias
import module_name as alias

# Importing all items (not recommended)
from module_name import *

# Creating a module
# Just save your Python code in a .py file

# Creating a package
# Create a directory with an __init__.py file
```

## File Handling

```python
# Reading a file
with open('file.txt', 'r') as f:
    content = f.read()

# Writing to a file
with open('file.txt', 'w') as f:
    f.write('Hello, World!')

# Appending to a file
with open('file.txt', 'a') as f:
    f.write('New line')
```

## Exception Handling

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exception occurred")
finally:
    print("This always executes")

# Raising an exception
raise ValueError("This is a custom error message")
```

## List Comprehensions

```python
# Basic list comprehension
squares = [x**2 for x in range(10)]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
```

## Lambda Functions

```python
# Basic lambda function
square = lambda x: x**2

# Used with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
```

## Built-in Functions

Some commonly used built-in functions:

- `print()`: Print to the standard output
- `len()`: Return the length of an object
- `type()`: Return the type of an object
- `range()`: Generate a sequence of numbers
- `enumerate()`: Return an enumerate object
- `zip()`: Create an iterator of tuples
- `sorted()`: Return a new sorted list
- `min()`, `max()`: Return the minimum or maximum value
- `sum()`: Sum of all items in an iterable
- `any()`, `all()`: Check if any or all items are True
- `filter()`: Construct an iterator from elements which are true
- `map()`: Apply a function to every item of an iterable

## Standard Library Modules

Some commonly used modules from the standard library:

- `os`: Operating system interface
- `sys`: System-specific parameters and functions
- `math`: Mathematical functions
- `random`: Generate random numbers
- `datetime`: Date and time functions
- `json`: JSON encoder and decoder
- `re`: Regular expressions
- `collections`: Specialized container datatypes
- `itertools`: Functions creating iterators for efficient looping
- `functools`: Higher-order functions and operations on callable objects
- `threading`: Thread-based parallelism
- `multiprocessing`: Process-based parallelism
- `sqlite3`: DB-API 2.0 interface for SQLite databases
- `urllib`: URL handling modules
- `csv`: CSV file reading and writing
- `pickle`: Python object serialization

## Type Hints

Type hints were introduced in Python 3.5 to provide optional static typing. They help with code readability, catching potential type-related errors, and improving IDE support.

### Basic Type Hints

```python
# For variables
age: int = 25
name: str = "Alice"
pi: float = 3.14
is_student: bool = True

# For functions
def greet(name: str) -> str:
    return f"Hello, {name}!"

# For collections
from typing import List, Dict, Tuple, Set

numbers: List[int] = [1, 2, 3]
person: Dict[str, str] = {"name": "Bob", "city": "New York"}
coordinates: Tuple[float, float] = (10.5, 20.7)
unique_numbers: Set[int] = {1, 2, 3}
```

### Optional and Union Types

```python
from typing import Optional, Union

def process_data(data: Optional[str] = None) -> None:
    if data is None:
        print("No data provided")
    else:
        print(f"Processing: {data}")

def handle_input(value: Union[int, str]) -> str:
    return str(value)
```

### Type Aliases

```python
from typing import List, Dict

Vector = List[float]
Matrix = List[Vector]
JSONObject = Dict[str, Union[str, int, float, bool, None]]

def scale_vector(v: Vector, scalar: float) -> Vector:
    return [x * scalar for x in v]
```

### Generic Types

```python
from typing import TypeVar, List

T = TypeVar('T')

def first_element(l: List[T]) -> T:
    return l[0]
```

### Callable Types

```python
from typing import Callable

def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    return operation(x, y)

def add(a: int, b: int) -> int:
    return a + b

result = apply_operation(5, 3, add)
```

### Type Comments (for Python 3.5+)

```python
# For older Python versions that don't support type annotations in function definitions
def legacy_function(x, y):
    # type: (int, int) -> int
    return x + y
```

### Type Checking

Python's type hints are not enforced at runtime. To check for type errors, you can use third-party tools like mypy:

```bash
pip install mypy
mypy your_script.py
```

