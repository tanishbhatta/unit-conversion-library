'''
Weight conversion module
'''

def kilogram_to_gram(kg:float) -> float:
    """
    Converts Kilogram into Gram

    Argument:
        kg: Mass measure in kilograms.
    
    Returns:
        Equivalent mass in grams.
    """
    g = kg * 1000

    return g

def gram_to_kilogram(g:float) -> float:
    """
    Converts Gram into Kilogram

    Argument:
        g: Mass measure in grams.
    
    Returns:
        Equivalent mass in kilograms.
    """
    kg = g / 1000

    return kg

def kilogram_to_pound(kg:float) -> float:
    """
    Converts Kilogram into Pound

    Argument:
        kg: Mass measure in kilograms.
    
    Returns:
        Equivalent mass in pounds.
    """
    lb = kg * 2.205

    return lb

def pound_to_kilogram(lb:float) -> float:
    """
    Converts Pound into Kilogram

    Argument:
        lb: Mass measure in pounds.
    
    Returns:
        Equivalent mass in kilograms.
    """
    kg = lb / 2.205

    return kg

def gram_to_ounce(g:float) -> float:
    """
    Converts Gram into Ounce

    Argument:
        g: Mass measure in grams.
    
    Returns:
        Equivalent mass in ounces.
    """
    oz = g / 28.35

    return oz

def ounce_to_gram(oz:float) -> float:
    """
    Converts Ounce into Gram

    Argument:
        oz: Mass measure in ounces.
    
    Returns:
        Equivalent mass in grams.
    """
    g = oz * 28.35

    return g

def ton_to_kilogram(ton:float) -> float:
    """
    Converts Ton into Kilogram

    Argument:
        ton: Mass measure in tons.
    
    Returns:
        Equivalent mass in kilograms.
    """
    kg = ton * 907.2

    return kg

def kilogram_to_ton(kg:float) -> float:
    """
    Converts Kilogram into Ton

    Argument:
        kg: Mass measure in kilograms.
    
    Returns:
        Equivalent mass in tons.
    """
    ton = kg / 907.2

    return ton
