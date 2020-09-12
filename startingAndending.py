# if x is present in arr[] then  
# returns the index of starting position  
# starting of x in arr[0..n-1], 
# otherwise returns 0  
def start(arr, low, high, x, n) : 
    if(high >= low) : 
        mid = low + (high - low) // 2
        if( ( mid == 0 or x > arr[mid - 1]) and arr[mid] == x) : 
            return mid 
        elif(x > arr[mid]) : 
            return start(arr, (mid + 1), high, x, n) 
        else : 
            return start(arr, low, (mid - 1), x, n) 
      
    return 0
  
  
# if x is present in arr[] then  
# returns the index of Ending position 
# of x in arr[0..n-1], otherwise 
# returns 0  
def end(arr, low, high, x, n) : 
    if (high >= low) : 
        mid = low + (high - low) // 2
        if (( mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x) : 
            return mid 
        elif (x < arr[mid]) : 
            return end(arr, low, (mid - 1), x, n) 
        else : 
            return end(arr, (mid + 1), high, x, n) 
              
    return 0

# Driver program 
arr = [5,7,7,9,9,10] 
n = len(arr) 
  
x = 9
print("Starting position = ", 
      start(arr, 0, n - 1, x, n)) 
print("Ending position = ", 
      end(arr, 0, n - 1, x, n)) 