'''
Distance conversion module
'''

def kilometer_to_meter(km:float) -> float:
    """
    Converts Kilometer into Meter

    Argument:
        km: Distance measure in kilometers.
    
    Returns:
        Equivalent distance in meters.
    """
    m = km * 1000

    return m

def meter_to_kilometer(m:float) -> float:
    """
    Converts Meter into Kilometer

    Argument:
        m: Distance measure in meters.
    
    Returns:
        Equivalent distance in kilometers.
    """
    km = m / 1000

    return km

def kilometer_to_mile(km:float) -> float:
    """
    Converts Kilometer into Mile

    Argument:
        km: Distance measure in kilometers.
    
    Returns:
        Equivalent distance in Miles.
    """
    mil = km / 1.609

    return mil

def mile_to_kilometer(mil:float) -> float:
    """
    Converts Mile into Kilometers

    Argument:
        mil: Distance measure in miles.
    
    Returns:
        Equivalent distance in kilometers.
    """
    km = mil * 1.609

    return km

def meter_to_foot(m:float) -> float:
    """
    Converts Meter into Foot

    Argument:
        m: Distance measure in meters.
    
    Returns:
        Equivalent distance in feet.
    """
    ft = m * 3.281

    return ft

def foot_to_meter(ft:float) -> float:
    """
    Converts Foot into Meter

    Argument:
        ft: Distance measure in feet.
    
    Returns:
        Equivalent distance in meters.
    """
    m = ft / 3.281

    return m

def centimeter_to_inch(cm:float) -> float:
    """
    Converts Centimeter into Inch

    Argument:
        cm: Distance measure in centimeters.
    
    Returns:
        Equivalent distance in inches.
    """
    inc = cm / 2.54

    return inc

def inch_to_centimeter(inc:float) -> float:
    """
    Converts Meter into Centimeter

    Argument:
        inc: Distance measure in inches.
    
    Returns:
        Equivalent distance in centimeters.
    """
    cm = inc * 2.54

    return cm
    