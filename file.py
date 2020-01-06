import re
def catch_password(password):
    """A program that matches a password

       password: the string to be matched"""
    valid_password = re.compile(r"[a-zA-Z(\d+)]{5,10}")
    if valid_password.search(password):
        return "Password correct"
    else:
        return "Password must be eight characters long, must contains both lowercase and uppercase letters "\
               "must contain at least one digit"

def count_steps(num):
    mode = [1,2,3,4,5,6,7,8,9]
    result = []
    for item in mode:
        result.append(num // item)
    steps = min(result)
    print("The shortest number of steps from 1 to {} is {} step(s)".format(num,steps))




def count_pairs(items):
    """

    :rtype: count of pairs in a sequence
    """
    try:
        count = 0
        for i in items:
            now = iter(items)
            if i == next(now):
                count += 1
            else:
                return None
        return count
    except IndexError:
        print("Can't iterate. list index out of range.")


def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)

def return_even(items):
    result = []
    for i in items:
        if i % 2 == 0:
            result.append(i)
        else:
            continue
    return sorted(result)

def power(a,n):
    return 1 if n == 0 else a * power(a,n-1)