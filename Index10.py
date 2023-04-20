def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
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
    if x1.isdigit():
        s=int(x1)
    if x2.isdigit():
        s=s+int(x2)
    if x3.isdigit():
        s=s+int(x3)
    if x4.isdigit():
        s=s+int(x4)
    if x5.isdigit():
        s=s+int(x5)
    return s
print(main("12k45"))