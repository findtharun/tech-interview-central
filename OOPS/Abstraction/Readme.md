## Abstraction

### Interface vs Abstract Class

- interfaces can have no state (variables - only Constants)  and a class that <b>implements</b> an interface must provide an implementation of all the methods of that interface.
    - From Java 8 Interfaces can have Methods Implemented in it.
    - From Java 8, an interface can declare an instance variable, but it must be a public static final variable, which means it is a constant value that cannot be changed by any implementation of the interface. Read more on Sarthaks.com - https://www.sarthaks.com/3492649/can-an-interface-have-instance-variables-in-java

- abstract classes may contain state (data members) and/or implementation (methods) - abstract classes can be inherited without implementing the abstract methods (though such a derived class is abstract itself) . Classes <b> extends</b> Abstract Classes.

- interfaces may be multiple-inherited, abstract classes may not (this is probably the key concrete reason for interfaces to exist separately from abtract classes - they permit an implementation of multiple inheritance that removes many of the problems of general MI).
