
def markdown_to_html_image(markdown_image: str) -> str:
    '''Converts a Markdown image link to an HTML image tag.

    Args:
        markdown_image (str): A string containing a Markdown image link.

    Returns:
        str: The corresponding HTML image tag.

    Examples:
    >>> markdown_to_html_image("![awesome dog](dog.jpg)")
    '<img src="dog.jpg" alt="awesome dog">'
    >>> markdown_to_html_image("![python logo](python.png)")
    '<img src="python.png" alt="python logo">'
    '''
    
    
    alt,src = markdown_image[2:-1].split("](")
    return f'<img src="{src}" alt="{alt}">'
    
# #Another Method:


# def markdown_to_html_image(markdown_image: str) -> str:
#     a=markdown_image.index("[")
#     b=markdown_image.index("]") 
#     c=markdown_image.index("(")
#     d=markdown_image.index(")")
    
#     return '<img src="'+markdown_image[c+1:d]+'" alt="'+markdown_image[a+1:b:]+'">'


# down Image to HTML Image
# Given a string containing a Markdown image link of the format ![alt text](image_url), convert it to a proper HTML image tag of the format <img src="image_url" alt="alt text">.

# Examples

# >>> markdown_to_html_image("![awesome dog](dog.jpg)")
# '<img src="dog.jpg" alt="awesome dog">'
# >>> markdown_to_html_image("![python logo](python.png)")
# '<img src="python.png" alt="python logo">'
