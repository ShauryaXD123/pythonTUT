# print(0 == False)
# print(1==True)

#conditional opr -> ==,<,>   >= , <= , != (not equals to)

# age = int(input("Enter your age "))

# if age >= 18 :
#     print("You can vote ")
# else:
#     print("You can't vote ")


trafficPolice = input("Enter required signal : (Red,Yellow,Green) :- ")

if trafficPolice == "Red" :
    print("stop")
elif trafficPolice=="Yellow":
    print("Ready")
elif trafficPolice=="Green":
    print("Go")
else:
    print("Invalid colour")        
