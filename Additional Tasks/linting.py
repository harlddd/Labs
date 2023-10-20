"""
linting test
"""
def count( sequence, item):
    """
    counts numbers    
    """
    itemcount = 0
    for n in sequence:
        if n == item:
            itemcount += 1
    return itemcount
