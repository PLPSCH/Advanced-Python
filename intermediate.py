while True:
    print("\n--- Simple Calculator---")
    num1=float(input("Enter First Number : "))
    num2=float(input("Enter Second Number : "))
    
    sum_result = num1+num2
    difference_result=num1-num2
    product_result=num1*num2
    
    if num2 != 0:
        quotient_result=num1/num2
        module_result=num1%num2
    else:
        quotient_result ="undefined (division by zero)"
        module_result="undefined (division by zero)"
    
    print("\nHere are your results : ")
    print(f"Sum : {sum_result}")
    print(f"Difference : {difference_result}")
    print(f"Product : {product_result}")
    print(f"Quotient : {quotient_result}")
    print (f"Module : {module_result}")
    choice = input("\n Do you want to perform another calculation? (yes/no): ")
    if choice.lower() !='yes':
        print ("Thank you for using the calculator. Goodbye !")
        break