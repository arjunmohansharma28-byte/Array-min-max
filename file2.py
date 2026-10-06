def minElement(a, size):
    temp =a[0]
    for i in range(1,size):
        temp = min(temp,a[i])
    return temp

def maxElement(a, size):
    temp = a[0]
    for i in range(1, size):
        temp = max(temp,a[i])
    return temp
a = [90, 89, 82, 186, 2]
size = len(a)
print("Min =",minElement(a,size))
print("Max =",maxElement(a,size))