# Students should edit this Python file (just as you would a Python cell in a Jupyter Notebook)
# this module will contain functions for numerical integration


def trapezoidal_rule(f, a, b, N):
    """Approximate the integral of f from a to b using the trapezoidal rule.

    Parameters
    ----------
    f : callable
        Function to integrate. It should accept a scalar input and return a float.
    a : float
        Lower limit of integration.
    b : float
        Upper limit of integration.
    N : int
        Number of slices to divide the interval into.

    Returns
    -------
    float
        Approximate value of the integral.
    """
    h = (b - a) / N
    total = 0.5 * f(a) + 0.5 * f(b)
    for i in range(1, N):
        x = a + i * h
        total += f(x)
    return total * h


def simpsons_rule(f, a, b, N):
    """Approximate the integral of f from a to b using Simpson's rule.

    Parameters
    ----------
    f : callable
        Function to integrate. It should accept a scalar input and return a float.
    a : float
        Lower limit of integration.
    b : float
        Upper limit of integration.
    N : int
        Number of slices to divide the interval into. Must be even.

    Returns
    -------
    float
        Approximate value of the integral.
    """
    if N % 2 != 0:
        raise ValueError("N must be even for Simpson's rule")
    h = (b - a) / N
    total = f(a) + f(b)

    for i in range(1, N):
        x = a + i * h
        weight = 4 if i % 2 != 0 else 2
        total += weight * f(x)

    return total * h / 3