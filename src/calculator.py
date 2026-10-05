def add(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    return x + y

def subtract(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def multiply(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
        Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def add_three_nums(x, y, z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    Raises:
        ValueError: If x, y, or z is not a number
    """
    if not all(isinstance(n, (int, float)) for n in (x, y, z)):
        raise ValueError("All inputs must be numbers")
    total_sum = x + y + z
    return total_sum

def divide(x, y):
    """
    Divides x by y
    Args:
        x (int/float): Numerator
        y (int/float): Denominator
    Returns:
        float: Quotient of x and y
    Raises:
        ValueError: If x or y is not a number or if y = 0
        """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers")
    if y == 0:
        raise ValueError("Cannot divide by 0")
    return x/y

def power(x, y):
    """
    Raises x to the power of y
    Args:
        x (int/float): Base
        y (int/float): Exponent
    Returns:
        int/float: x raised to the power of y
    Raises:
        ValueError: If x or y is not a number
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return x**y

def average(numbers):
    """
    Calculates the mean of a list of numbers
    Args:
        numbers (list): a list of int/float values
    Returns:
        float: The average of the numbers
    Raises:
        ValueError: If the list is empty or contains a non-number
    """
    if len(numbers) == 0:
        raise ValueError("Cannot average an empty list")
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise ValueError("All items must be numbers")
    return sum(numbers)/len(numbers)


