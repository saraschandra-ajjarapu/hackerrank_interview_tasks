# Python: Return or Raise ValueError

# Implement a function, multiply, that takes 3 integer arguments a,b and bound.

# 1) If the result of multiplying a and b is less than or equal to bound the function returns the result.

# 2) If the result of multiplying a and b is greater than bound, the function raises a ValueError exception with the following message:if a =2,b=5 and bound=8, then the message must be:"multiplication of 2 and 5 with bound 8 is not possible"

def multiply(a,b,bound):
    num = a*b
    if a*b > bound:
        raise ValueError("multiplication of " + str(a)+ " and " + str (b) + "with bound " + str(bound) + " not possible" )
    else:
        return num
        