## Method Overloading

Method / Function Overloading is about 2 Things

- Various Data Types of Parameters in Same function
- No.of Arguments

### Java vs Python

Python does not support method overloading by default, but we can implement easily.

- In terms of Data Types : It defats whole purpose of python as it is dynamically typed langauge, hence by default overloading is not supported.
- In terms of No.of Arguments
  - Python Supports (*args) which can be used to implement Overloading (https://www.geeksforgeeks.org/args-kwargs-python/)
  - We can also Implement Default Variable value as None and Implement overloading. (https://www.codecademy.com/learn/learn-intermediate-python-3/modules/int-python-function-arguments/cheatsheet)


## Method Overriding

When a child class method overrides(or, provides it's own implementation) the parent class method of the same name, parameters and return type, it is known as method overriding.

### Java vs Python

- Java does not support Multiple Inheritance. (Diamond Problem : https://www.geeksforgeeks.org/diamond-problem-in-java/) , Can be resolved by using Interfaces (We Implement Ambiguous function in class where we initialize thus removes confusion)
- Python Supports Multiple Inheritance, It resolves ambiguity based on the order which class was declared.

```
class A()

class B(A)

class C(A)

class D(B,C)

in this case Class D will pick functions from B , since it was first Interpreted.

```