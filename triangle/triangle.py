def equilateral(sides):
    """
    # An _equilateral_ triangle has all three sides the same length.
    """
    if 0 in sides:
        return False
    return all(sides[0] == side for side in sides)


def isosceles(sides):
    """
    # An _isosceles_ triangle has at least two sides the same length.
    """
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]


def scalene(sides):
    """
    # A _scalene_ triangle has all sides of different lengths.
    """
    oneThird = sum(sides) / 3
    return oneThird != sides[0] or oneThird != sides[1] or oneThird != sides[2]
