"""Arithmetic operations for the numeric-based calculator."""

class Operations:
    """Provides static methods for basic arithmetic."""

    @staticmethod
    def add(x, y):
        """Return the sum of x and y."""
        return x + y

    @staticmethod
    def subtract(x, y):
        """Return the difference of x and y."""
        return x - y

    @staticmethod
    def multiply(x, y):
        """Return the product of x and y."""
        return x * y

    @staticmethod
    def divide(x, y):
        """
        Return x / y, raising ZeroDivisionError if y == 0.

        Raises:
            ZeroDivisionError: If y == 0.
        """
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return x / y
