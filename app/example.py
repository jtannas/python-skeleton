#!/usr/bin/python3.6
"""Example Module Docstring

Say something about what the module is for. Docstring line limit 72ish.
"""

### IMPORTS ###################################################################


### SECTION DELIMETER #########################################################
def main():
    """
    My Example function prints 'Hello, world'

    Args:
        None (None): Does not require any arguments

    Returns:
        Prints 'Hello, world'

    Examples:
        >>> main()
        Hello, world

    """
    print('Hello, world')


def greeting(name: str='world') -> str:
    """
    Return a greeting incorporating the provided name.

    This function serves as an example of Python3 type checking

    Args:
        name (str): Name to be greeted

    Returns:
        greeting (str): A greeting text

    Raises:
        TypeError: if name is not a string

    Examples:
        >>> greeting('Jack')
        'Hello, Jack'

        >>> greeting('Jill')
        'Hello, Jill'

        >>> greeting(1)
        Traceback (most recent call last):
        ...
        TypeError: must be str, not int

    """
    return 'Hello, ' + name


if __name__ == "__main__":
    main()
