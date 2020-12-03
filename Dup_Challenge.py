# Python 3 Count Duplicate Elements 

# Given an integer array, numbers, count the number of elements that oocue more than once.

# Example : numbers = [1,3,3,4,4,4] : There are two non unique elements : 3 and 4 , Sample Output : 2

def  countDuplicate(numbers):
    from collections import Counter
    ans = []
    cnt = Counter(numbers)
    for k, v in cnt.items():
        if v > 1:
            ans.append(k)
    return len(ans)