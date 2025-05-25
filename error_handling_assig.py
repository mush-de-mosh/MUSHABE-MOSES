while True:
    numbers = input("Enter two numbers seperated by a comma i.e: 1,2\n")
    arr = numbers.split(',')
    print(arr)
    
    num1 = int(arr[0])
    num2 = int(arr[1])

    
    if (num1 == 0 and num2 == 0):
        print("Don't enter two zeros!\n")
    else:
        try:
            result = num1/num2
            break
        except Exception:
            print("You cannot divide with a zero!")  
              
print(f"The answer is {result}!")         
    