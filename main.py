
def sumArray(arr):
    sum = 0;
    for i in range(0, len(arr)):
        sum += int(arr[i])
    return sum

def productArray(arr):
    product = 1;
    for i in range(0, len(arr)):
        product *= int(arr[i])
    return product

def reverseArray(arr):
    return arr[::-1]



print("Enter numbers separated by spaces:")
arr = input().split()
print("Sum: " + str(sumArray(arr)))
print("Product: " + str(productArray(arr)))
print("Reversed: " + str(reverseArray(arr)))