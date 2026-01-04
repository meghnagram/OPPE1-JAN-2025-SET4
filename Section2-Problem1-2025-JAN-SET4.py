
def first_non_repeating_char(s: str)->str:
    """Finds the first non-repeating character in a string."""
    
    
    # Using count
    # char_count = {}
    # for char in s:
    #     char_count[char] = char_count.get(char, 0) + 1
    
    # for char in s:
    #     if char_count[char] == 1:
    #         return char

    # Using seen and substring check
    seen = set()
    for i in range(len(s)):
        # check if current char is not in remaining char
        if s[i] not in seen and s[i] not in s[i+1:]:
            return s[i]
        seen.add(s[i])

#     #AnotherMethod:

# def first_non_repeating_char(s: str)->str:
#     l=list(s)
#     c=0

#     for i in l:
#         maxi=l.count(i)
#         if maxi==1:
#             return(i)
#     return None


# First Non-Repeating Character in a String
# Write a function first_non_repeating_char(s) that returns the first non-repeating character in the string s. If no such character exists, return None.

# Example

# >>> s = "abcab" # c is the only non repeating char
# >>> first_non_repeating_char(s)
# 'c'
# >>> s = "aabbcc"
# >>> first_non_repeating_char(s) # all chars are repeating
# None
# >>> s = "buzzingbee" # u, i, n and g are non repeating and first is "u"
# >>> first_non_repeating_char(s)
# 'u'
  
            
