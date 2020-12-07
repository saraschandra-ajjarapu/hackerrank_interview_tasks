def moveZerosToEnd(arr,n):
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count+=1
    while count < n:
        arr[count]=0
        count += 1
arr = [3,5,7,0,1,0,9]
n = len(arr)
moveZerosToEnd(arr,n)
print("Array after pushing all zeros to end: ")
print(arr)       