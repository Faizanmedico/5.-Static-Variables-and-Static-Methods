# 5.-Static-Variables-and-Static-Methods
5. Static Variables and Static Methods


Assignment:
Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

Explanation:

@staticmethod Decorator:

This decorator is used to define a static method.

A static method does not receive self (the instance) or cls (the class) as its first argument.

It cannot access or modify instance state (instance variables) or class state (class variables). Its behavior is independent of any specific instance or the class itself.

add(a, b) Method:

This method takes two arguments, a and b, and simply returns their sum.

As per the assignment, it does not use any class variables (like MathUtils.some_variable) or instance variables (self.some_variable). It operates solely on the input parameters.

Calling the Static Method:

You call a static method directly on the class itself: MathUtils.add(5, 3).

This is a key characteristic of static methods: you don't need to create an object of the MathUtils class to use its add functionality. This makes them ideal for utility functions 
