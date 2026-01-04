
def remove_n_elems_from_index(t: tuple, n: int, i: int) -> tuple:
    """
    Removes n elements from a tuple starting from a given index.

    Args:
        t (tuple): The input tuple.
        n (int): The number of elements to remove.
        i (int): The index to remove elements from.

    Returns:
        tuple: A new tuple with the specified elements removed.
    """
    
    return t[:i] + t[i + n:]

# #Another Method:

# def remove_n_elems_from_index(t: tuple, n: int, i: int) -> tuple:
#     s=list(t)
#     l=[]
#     c=0
    
#     for j in range(len(s)):
#         if i<=j <=i+n-1:
#             continue
#         else:
#             l.append(s[j])
            
#     return tuple(l)

# Remove n Elements from the Given Index
# Write a function remove_n_elems_from_index that takes a tuple t, an integer n, and an index i as input. The function should return a new tuple with the n elements starting at index i removed. If the index i is out of bounds, return the original tuple.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Examples

# >>> remove_n_elems_from_index((1, 2, 3, 4, 5), 2, 1)
# (1, 4, 5)
# >>> remove_n_elems_from_index((10, 20, 30, 40, 50), 3, 2)
# (10, 20, 30)
# >>> remove_n_elems_from_index((1, 2, 3, 4, 5), 5, 0)
# ()
        
    
