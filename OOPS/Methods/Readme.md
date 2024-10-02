# Comparison of Normal Methods, Class Methods, and Static Methods in Java vs Python

| Feature                     | Java                                             | Python                                               |
|-----------------------------|--------------------------------------------------|------------------------------------------------------|
| **Normal Methods** (Instance Methods) | Defined within a class and can access instance data. Called on an instance. | Defined within a class, with `self` as the first parameter. Called on an instance. |
| **Class Methods**            | No direct equivalent. Can simulate with static methods or class constructors. | Defined using `@classmethod`, takes `cls` as the first parameter, operates at the class level. |
| **Static Methods**           | Declared using `static`. No access to instance data or methods. Can be called on the class. | Defined using `@staticmethod`. No access to class or instance data. Called on the class. |

## Key Differences

1. **Normal Methods (Instance Methods)**:
   - **Java**: Normal methods are bound to an instance and require object creation to be invoked. `this` is implicit.
   - **Python**: Normal methods are defined with `self`, which refers to the instance. `self` must be explicitly included.
   - Use when the method operates on instance-specific data or modifies the object's state.

2. **Class Methods**:
   - **Java**: Class methods are not directly supported. Static methods or constructors can be used to mimic class-level behavior.
   - **Python**: Class methods are supported via `@classmethod` decorator, where the first parameter `cls` refers to the class itself.
   - Use when the method operates on class-level data or when alternative constructors are needed

3. **Static Methods**:
   - **Java**: Static methods are defined with the `static` keyword and do not need an instance. They can only access other static members.
   - **Python**: Static methods are defined with `@staticmethod` decorator. They do not have access to `self` or `cls` and act as regular functions inside a class.
   - Use when the method does not depend on either the instance or class data but is logically related to the class.

Best Explanation : [Corey Schafer OOPs Tutorial](https://www.youtube.com/watch?v=rq8cL2XMM5M)