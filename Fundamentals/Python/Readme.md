## Key Features of Python

- Dynamically Typed
- Functions and Classes are First Class Objects
- Python supports all OOPs features, including Composition
- No explicit access modifiers (private , public etc..), but we can restrict. By Default all are public
  - _var (Protected) - Can be accessed by subclasses
  - __var (Private) - can be accessed only by class
- Interpreted (Compiled & Interpreted)

When you run a Python program, the Python interpreter first compiles the source code into bytecode. Bytecode is a low-level representation of the Python program that is easier for the interpreter to execute. The interpreter then executes the bytecode line by line.

It is compiled because the source code is converted into bytecode. It is interpreted because the bytecode is executed line by line.

The compilation step in Python is mostly hidden from the user. You do not need to compile a Python program before you can run it. The interpreter will compile the program for you automatically when you run it.

However, there are some cases where you may want to compile a Python program yourself. For example, you may want to compile a Python program into a standalone executable file.

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

```
Arugments are passed by Reference (Object Reference)
```

## Iterators

Iterator is an object that represents a stream of data. It implements the iterator protocol, which consists of two methods: __iter__() and __next__(). Iterators are used to iterate over elements in a sequence, such as lists, tuples, dictionaries, and more

Built-in Iterators
Python provides built-in functions and classes that return iterators or work with iterators:

- iter(): Returns an iterator from an iterable object.
- next(): Retrieves the next item from an iterator.
- enumerate(): Returns an iterator of tuples containing indices and items from an iterable.
- zip(): Returns an iterator that aggregates elements from multiple iterables.
- map() and filter(): Return iterators that apply a function to each element in an iterable or filter elements based on a function, respectively.