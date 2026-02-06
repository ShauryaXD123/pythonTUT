#this is a program to generate a marksheet

print("drdonut's marksheet generator ")
Name=input("Enter student's name")
rollNo=int(input("Enter student's roll no"))
print("Enter student's marks ")

Maths=float(input( "Enter maths marks "))
Science=float(input("Enter science marks"))
English=float(input("Enter english marks "))
Hindi=float(input("Enter hindi marks "))
Sst=float(input("Enter sst marks "))

# avg = total sum/units
sum=Maths+Science+English+Hindi+Sst
Average=sum/5

print("---------Mark Sheet---------")

print("student name : ",Name)
print("rollNo : ",rollNo)

print("Maths : ",Maths)
print("Science: ",Science)
print("English: ",English)
print("Hindi: ",Hindi)
print("Sst: ",Sst)

print("result avg : ",Average)
