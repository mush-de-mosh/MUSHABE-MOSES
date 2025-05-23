def factorial(x) -> int:
    if(x>0):
       result = x*factorial(x-1)
       return result
    else:
        return 1   

#factorial of 5
print(factorial(0))