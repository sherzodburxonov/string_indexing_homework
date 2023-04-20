def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x1=s[0]
    x2=s[1]
    x3=s[2]
    x4=s[3]
    x5=s[4]
    s=0
    if x1.isdigit():
        s=s+1
    if x2.isdigit():
        s=s+1
    if x3.isdigit():
        s=s+1
    if x4.isdigit():
        s=s+1
    if x5.isdigit():
        s=s+1
    return s
    
print(main("sf478"))