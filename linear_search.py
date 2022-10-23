##worst case O(n) 
def search(arr, x):

    for i in range(len(arr)):
 
        if arr[i] == x:
            return True# returned when x is present
 
    return False##returned when x is absent
arr=[45,67,89,90,99,678]
x=90
x=900
print(search(arr,x))