## Key Features of Python

- Interpreted , Dynamically Typed
- Functions and Classes are First Class Objects
- Python supports all OOPs features, including Composition
- No access modifiers (private , public etc..)

## DataTypes

- Immutable - Objects are of in-built datatypes like int, float, bool, string, Unicode, and tuple.
- Mutable - Lists, Dictionaries and Sets
- Zip function in Python is a built-in utility that allows you to combine multiple iterables (like lists, tuples, etc.) into a single iterator of tuples. Each tuple contains elements from the corresponding positions of the input iterables. It's often used for parallel iteration.

```
# Example lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Using zip
zipped = zip(list1, list2)
print(list(zipped))
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]
```

- Methods vs Functions : Methods are Defined in Class , can only be accessed by Object. Functions are Independent are written outside of classes. More details can be found here : https://www.educative.io/answers/what-is-the-difference-between-a-method-and-a-function

## Variables

Local / Instance , Class, Global

- Python do not have concept of static, class variables are equivalent to static variables.
- Python supports global variables, it variable is global only within the module where it is defined. To access it across different modules, import the module containing the global variable.

## Methods

- Instance Methods: Operate on instances of the class.
- Abstract Methods: Must be implemented by subclasses.
- Final Methods: Cannot be overridden by subclasses.
- Class Methods
  - we can Modify class Variables with help of class Methods.
  - we can make alternative constructor using class Methods. Sometimes people have information of their specific instances of the class available in a
- Static Methods
  - These are methods that have a logical connection to the Class, but does not need a class or instance as an argument.
  - They do not directly access class/ Instance variables.
