def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if len(s)>=n:
        x=s[n]
    else :
        x=False 
    return x
print(main("good",3))
