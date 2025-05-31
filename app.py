class MathUtils:
    """
    A utility class for mathematical operations, specifically addition,
    using a static method.
    """

    @staticmethod
    def add(a, b):
        """
        A static method that returns the sum of two numbers.
        It does not access any class or instance variables.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The sum of a and b.
        """
        return a + b

# You can call a static method directly using the class name,
# without creating an instance of the class.
print(f"Sum of 5 and 3: {MathUtils.add(5, 3)}")
print(f"Sum of 10.5 and 7.2: {MathUtils.add(10.5, 7.2)}")
print(f"Sum of -4 and 9: {MathUtils.add(-4, 9)}")

# Although it's less common for static methods, you *can* call them
# from an instance as well, but it's not the primary use case.
# instance = MathUtils()
# print(f"Sum of 2 and 7 (via instance): {instance.add(2, 7)}")