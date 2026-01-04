
def is_obtuse(theta_1: int, theta_2: int) -> bool:
    '''
    Check if a triangle is obtuse given two angles.

    Args:
        theta_1 (int): The first angle of the triangle.
        theta_2 (int): The second angle of the triangle.

    Returns:
        bool: True if the triangle is obtuse, False otherwise.

    Examples:
    >>> is_obtuse(30, 60)
    False
    >>> is_obtuse(30, 30)
    True
    >>> is_obtuse(100, 40)
    True
    >>> is_obtuse(60, 45)
    False
    '''
    
    return (theta_1 > 90 or theta_2 > 90 or (theta_1 + theta_2) < 90)

# #Another Method

# def is_obtuse(theta_1: int, theta_2: int) -> bool:
   
#     c=180-(theta_1+theta_2)
#     if theta_1>90 or theta_2>90 or c>90:
#         return True
#     else:
#         return False

# Check if a Triangle is Obtuse
# Given two angles of a triangle (theta_1 and theta_2) in degrees, determine if the triangle is obtuse. A triangle is obtuse if it has one angle greater than 90 degrees.

# Examples

# >>> is_obtuse(30, 60) # other angle is 90 so right triangle
# False
# >>> is_obtuse(100, 40) # has an angle 100, so obtuse
# True
# >>> is_obtuse(30, 30) # other angle is 120, so obtuse
# True
# >>> is_obtuse(60, 45) # other angle is 75, so acute
# False
    

