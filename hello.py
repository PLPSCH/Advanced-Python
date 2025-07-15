num1=float(input("enter the first number : "))
num2=float(input("enter the second number : "))
sum_result=num1+num2
difference_results=num1-num2
product_results=num1*num2

if num2 !=0:
   divide_results=num1/num2
else:
   divide_results="undefined (cant divide by zero)"  
if num2 !=0:
   module_results=num1%num2
else:
   module_results="undefined (cant return division by zero)"

print("\n here is your results ")
print(f"sum : {sum_result}")
print(f"difference : {difference_results}")
print(f"product : {product_results}")
print(f"divide : {divide_results}")
print(f"module : {module_results}")