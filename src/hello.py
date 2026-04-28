def hello_world(num: int) -> None:
    """
    A simple function that prints "Hello, world!" to the console.

    Parameters
    ----------
    num : int
        An integer parameter that is not used in the function.

    Returns
    -------
    None
         This function does not return anything.

    Examples
    --------
    >>> hello_world(5)
    Hello, world!
    Hello, world!
    Hello, world!
    Hello, world!
    Hello, world!
    """
    for i in range(num):
        print("Hello, world!")
