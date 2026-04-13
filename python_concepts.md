# Python Concepts Learned — Haunted House Project

## Classes and Objects (OOP)
- `class` keyword to define a class
- `__init__` method runs automatically when an object is created
- `self` refers to the object itself
- Attributes are variables attached to an object (`self.health = 100`)
- Methods are functions inside a class
- **Composition** — objects can contain other objects (e.g. `Room` has an `Inventory`)

## Data Types
- `None` — represents the absence of a value (not the string `"None"`)
- `float('inf')` — represents infinity (used for Zombie's HP)
- `str()` — converts a value to a string
- `int()` — converts a string to an integer

## Dictionaries (Java: `HashMap`)
- Created with `{}` (curly braces with key-value pairs)
- Access a value by key: `dictionary[key]`
- Check if a key exists: `key in dictionary`
- `.get(key, default)` — safely get a value with a fallback
- `.keys()` — returns all keys
- `.values()` — returns all values
- `.items()` — returns key-value pairs for looping
- `del dictionary[key]` — removes a key

## Lists (Java: `ArrayList`)
- Created with `[]`
- `.append(item)` — adds item to the end
- `.pop()` — removes and returns the last item
- `[-1]` — accesses the last item
- `len(list)` — returns the number of items
- Check if item exists: `item in list`
- **List comprehension** — shorthand for building lists: `[x for x in items if condition]`

## Control Flow
- `if / elif / else` — conditional branching
- `while` loop — repeats while a condition is true
- `for` loop — iterates over a sequence
- `return` — exits a method and optionally returns a value
- `break` — exits a loop early (not used yet but related)

## Logical Operators
- `and` — both conditions must be true (short-circuits: stops at first `False`)
- `or` — at least one condition must be true
- `not` — inverts a condition
- `is not None` — checks if something exists

## Comparison Operators
- `==` equal to
- `!=` not equal to
- `<=` less than or equal to
- `>=` greater than or equal to
- `in` — checks membership in a list or dictionary

## Functions and Methods
- Methods inside a class take `self` as the first parameter
- Calling a method requires `()` — without them you just reference it, not call it
- Methods can take arguments: `def method(self, arg):`
- Default arguments: `def add(self, name, qty=1):`

## The `random` Module
- `import random`
- `random.randint(a, b)` — random integer between a and b (inclusive)
- `random.choice(list)` — picks a random item from a list
- Modulo (`%`) with randint to control probability (e.g. `% 2 == 0` for ~50%)

## Strings
- Concatenation with `+`
- Must convert non-strings with `str()` before concatenating
- f-strings: `f"{variable}: {value}"` — cleaner way to format strings
- `"\n"` — newline character
- `"=" * 40` — repeats a string 40 times

## Input / Output
- `print()` — displays text in the terminal
- `input("prompt")` — asks the user for input, always returns a string

## Imports
- `from module import ClassName` — imports a specific class
- `import random` — imports the random module

## Type Conversion
- `str(value)` — converts to string
- `int(value)` — converts string to integer (crashes if not a valid number)

## Git Basics
- `git init` — initializes a repository
- `git add .` — stages all files
- `git commit -m "message"` — saves a snapshot
- `git push` — uploads to GitHub
- `.gitignore` — tells Git which files to ignore (e.g. `__pycache__/`)

## Common Bugs Encountered
- Using `|` instead of `or` for logical OR
- Forgetting `()` when calling a method
- Comparing a string to `None` with `==` instead of `is not None`
- Using a class name instead of an instance attribute
- Accessing `list[-1]` on an empty list
- `return` inside a loop or method stopping execution before a check runs
- Case sensitivity in string comparisons (e.g. `"fire"` vs `"Fire"`)
- Using dot notation on a dictionary instead of bracket notation
