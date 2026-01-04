

def difference(data: list) -> list:
    """Returns a list of differences between consecutive elements in the input list.

    Args:
        data (list[float]): The list of numerical values.

    Returns:
        list[float]: A list of differences between consecutive elements.
    """
    
    
    return [data[i] - data[i-1] for i in range(1, len(data))]
    

def nth_order_difference(data: list, n: int) -> list:
    """Returns a list of nth order differences between consecutive elements in the input list.

    Args:
        data (list[float]): The list of numerical values.
        n (int): The order of the difference.

    Returns:
        list[float]: A list of nth order differences.
    """
    
    
    for i in range(n):
        data = difference(data)
    return data
    

def has_positive_trend(data: list) -> bool:
    """Returns True if the list has a positive trend, False otherwise.

    Args:
        data (list[float]): The list of numerical values.

    Returns:
        bool: True if the list has a positive trend, False otherwise.
    """
    
    
    return all(map(lambda x: x >= 0, difference(data)))
    

def moving_average(data: list, window_size: int) -> list:
    """Returns a list of moving averages of the input data with the given window size.

    Args:
        data (list[float]): The list of numerical values.
        window_size (int): The window size for the moving average.

    Returns:
        list[float]: A list of moving averages.
    """
    
    
    if len(data) < window_size:
        return []
    moving_averages = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        moving_averages.append(sum(window) / window_size)
    return moving_averages
    

def has_negative_average_trend(data: list, window_size: int) -> bool:
    """Returns True if the list has a negative trend after applying moving average with the given window size.

    Args:
        data (list): The list of numerical values.
        window_size (int): The window size for the moving average.

    Returns:
        bool: True if the average trend is negative, False otherwise.
    """
    
    
    return all(map(lambda x: x <= 0, difference(moving_average(data, window_size))))


# #Another Method



# def difference(data: list) -> list:
#     """Returns a list of differences between consecutive elements in the input list.

#     Args:
#         data (list[float]): The list of numerical values.

#     Returns:
#         list[float]: A list of differences between consecutive elements.
#     """
#     pre=data[0]
#     l=[]
    
#     for i in range(1,len(data)):
#         l.append(data[i]-pre)
#         pre=data[i]
#     return l
    

# def nth_order_difference(data: list, n: int) -> list:
#     """Returns a list of nth order differences between consecutive elements in the input list.

#     Args:
#         data (list[float]): The list of numerical values.
#         n (int): The order of the difference.

#     Returns:
#         list[float]: A list of nth order differences.
#     """
#     newlist=data.copy()
#     for j in range(n):
#         m=difference(newlist)
#         newlist=m.copy()
        
#     return m
    

# def has_positive_trend(data: list) -> bool:
#     """Returns True if the list has a positive trend, False otherwise.

#     Args:
#         data (list[float]): The list of numerical values.

#     Returns:
#         bool: True if the list has a positive trend, False otherwise.
#     """
#     m=difference(data)
#     for i in range(len(m)):
#         if m[i]>=0:
#             pass
#         else:
#             return False
#     return True
#     # mini=min(m)
#     # if mini<0:
#     #     return False
#     # else:
#     #     return True
    
# def moving_average(data: list, window_size: int) -> list:
#     """Returns a list of moving averages of the input data with the given window size.

#     Args:
#         data (list[float]): The list of numerical values.
#         window_size (int): The window size for the moving average.

#     Returns:
#         list[float]: A list of moving averages.
#     """
#     l=len(data)
#     sublist=[]
#     finallist=[]
    
#     index=l-window_size
    
#     for i in range(index+1):
#         sublist=data[i:i+window_size]
#         avg=round(sum(sublist)/window_size,1)
#         finallist.append(avg)
        
#     return finallist
        
    

# def has_negative_average_trend(data: list, window_size: int) -> bool:
#     """Returns True if the list has a negative trend after applying moving average with the given window size.

#     Args:
#         data (list): The list of numerical values.
#         window_size (int): The window size for the moving average.

#     Returns:
#         bool: True if the average trend is negative, False otherwise.
#     """
    
#     m=moving_average(data,window_size)
#     m=difference(m)
#     for i in range(len(m)):
#         if m[i]<=0:
#             pass
#         else:
#             return False
#     return True

# Time Series Analysis
# Given a list of numerical values, implement the following functions to analyze its trend:

# difference(data: list) -> list: Returns a list of differences between consecutive elements in the input list.
# nth_order_difference(data: list, n: int) -> list: Returns a list of nth order differences between consecutive elements in the input list.
# has_positive_trend(data: list) -> bool: Returns True if the list has a positive trend, False otherwise.
# moving_average(data: list, window_size: int) -> list: Returns a list of moving averages of the input data with the given window size.
# has_negative_average_trend(data: list, window_size: int) -> bool: Returns True if the list has a negative trend after applying a moving average with the given window size.
# Example

# data1 = [1, 3, 5, 7, 9]
# data2 = [10, 8, 6, 4, 2]
# data3 = [1, 2, 1, 0, -1]

# print(has_positive_trend(data1))  # True
# print(has_positive_trend(data3))  # False
# print(difference(data1))           # [2, 2, 2, 2]
# print(nth_order_difference(data1, 2))  # [0, 0, 0]
# print(moving_average(data1, 3))    # [2.0, 4.0, 6.0, 8.0]
# print(has_negative_average_trend(data2, 2))  # True
# Moving Average Example

# >>> l = [1,2,3,4,5,6,7,8,9] 
# >>> window_size = 4
# # [1,2,3,4] -> 10/4 -> 2.5
# # [2,3,4,5] -> 14/4 -> 3.5
# # [3,4,5,6] -> 18/4 -> 4.5
# # [4,5,6,7] -> 22/4 -> 5.5
# # [5,6,7,8] -> 26/4 -> 6.5
# # [6,7,8,9] -> 30/4 -> 7.5
# >>> moving_average(l, window_size)
# [2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
    

