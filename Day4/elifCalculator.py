# + - * / avrg perc power

import math

print("`````````````this an advance calculator``````````````")
print("Enter required operation no. :- ")
print("1 for addition \n2 for substraction\n3 for multiplication\n4 for divisions\n5 for avrg\n6 for percent\n7 for power")
option=int(input("Enter option no. "))

if option==1:
    print("Enter numbers for addition")
    num1=float(input("Enter first number "))
    num2=float(input("Enter second number "))
    print(f"The sum of {num1} and {num2} is {num1+num2}")

elif option==2:
    print("Enter numbers for substraction")
    num1=float(input("Enter first number "))
    num2=float(input("Enter second number "))
    print(f"The sub of {num1} and {num2} is {num1-num2}")

elif option==3:
    print("Enter numbers for multiplication")
    num1=float(input("Enter first number "))
    num2=float(input("Enter second number "))
    print(f"The mul of {num1} and {num2} is {num1*num2}")

elif option==4:
    print("Enter numbers for division")
    num1=float(input("Enter first number "))
    num2=float(input("Enter second number "))
    print(f"The div of {num1} and {num2} is {num1/num2}")

elif option==5:
    print("Enter numbers for average")
    num1=float(input("Enter total sum"))
    num2=float(input("Enter number of terms "))
    print(f"The avg of {num1} and {num2} is {num1/num2}")

elif option==6:
    print("Enter numbers for percent")
    num1=float(input("Enter total sum "))
    num2=float(input("Enter out of "))
    print(f"The percentage of {num1} out of {num2} is {(num1/num2)*100}%")

elif option==7:
    print("Enter numbers for power")
    num1=float(input("Enter base "))
    num2=float(input("Enter power "))
    print(f"The power of {num1} to {num2} is { math.pow(num1,num2) }")

else :
    print("invalid option")




   


    
