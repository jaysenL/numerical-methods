def gradient_descent(grad_f, x0, learning_rate, n_steps):
    """Perform gradient descent on a one-dimensional function.

    Parameters
    ----------
    grad_f : callable
        Function that returns the gradient df/dx at a given x.
    x0 : float
        Initial value of x.
    learning_rate : float
        Step size for each update.
    n_steps : int
        Number of gradient descent steps to perform.

    Returns
    -------
    tuple[float, list[float]]
        The final x value and a list of x values at each step, including x0.
    """
    x = x0
    history = [x]
    for _ in range(n_steps):
        x = x - learning_rate * grad_f(x)
        history.append(x)
    return x, history
