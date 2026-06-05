'''
Temperature conversion module
'''

def celsius_to_fahrenheit(c:float) -> float:
    """
    Converts Celsius into Fahrenheit

    Argument:
        c: Temperature measure in celsius.
    
    Returns:
        Equivalent temperature in fahrenheit.
    """
    f = (c * 1.8) + 32

    return f

def fahrenheit_to_celsius(f:float) -> float:
    """
    Converts Fahrenheit into Celsius

    Argument:
        f: Temperature measure in fahrenheit.
    
    Returns:
        Equivalent temperature in celsius.
    """
    c = (f - 32) / 1.8

    return c

def celsius_to_kelvin(c:float) -> float:
    """
    Converts Celsius into Kelvin

    Argument:
        c: Temperature measure in celsius.
    
    Returns:
        Equivalent temperature in kelvin.
    """
    k = c + 273.15

    return k

def kelvin_to_celsius(k:float) -> float:
    """
    Converts Kelvin into Celsius

    Argument:
        k: Temperature measure in kelvin.
    
    Returns:
        Equivalent temperature in celsius.

    Constraint:
        Input must be greater or equal to zero.
    """
    if k < 0:
        raise ValueError("Invalid token")
    else:
        c = k - 273.15

        return c

def kelvin_to_fahrenheit(k:float) -> float:
    """
    Converts Kelvin into Fahrenheit

    Argument:
        k: Temperature measure in kelvin.
    
    Returns:
        Equivalent temperature in fahrenheit.
    
    Constraint:
        Input must be greater or equal to zero.
    """
    if k < 0:
        raise ValueError("Invalid token")
    else:
        f = (k - 273.15) * 1.8 + 32

        return f

def fahrenheit_to_kelvin(f:float) -> float:
    """
    Converts Fahrenheit into Kelvin

    Argument:
        f: Temperature measure in fahrenheit.
    
    Returns:
        Equivalent temperature in kelvin.
    """
    k = (f - 32) / 1.8 + 273.15

    return k