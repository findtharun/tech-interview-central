## Inheritance

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
