def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.isdigit():
        x=str(s)
    else :
        x=-1
    return x
print(main("k"))