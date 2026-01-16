# Write a program to find the GCD (Greatest Common Divisor) of an array of numbers.

def gcd(a,b):
    #euclidean algorithm
    while b != 0:
        a,b =b ,a % b
    return a

def gcd_of_array(arr):
    result = arr[0]   

    for i in range(1,len(arr)):
        result = gcd(result,arr[i]) 
    return result

number = list(map(int,input("enter numbers seperated by space: ").split()))    
print("GCD of the array:",gcd_of_array(number))