def equilateral(sides):
    """
    # An _equilateral_ triangle has all three sides the same length.
    """
    
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """
    # An _isosceles_ triangle has at least two sides the same length.
    """
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]


def scalene(sides):
    """
    # A _scalene_ triangle has all sides of different lengths.
    """
    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
