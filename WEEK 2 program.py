#1)greeting
name=str(input("Hello,what is your name :"))
print("Hello",name,"Good to meet you!")


#2)temperature
Fahren=float(input("Enter the temperature in Celsius :"))
temp=(Fahren*(9/5))+32
print(f"{Fahren}C is equivalent to {temp}F")

#3)group division
stn=int(input("How many students?"))
size=int(input("Required group size?"))
groups= stn//size
stn_left= stn%size
print(f"There will be {groups}, groups with  {stn_left} will be left over")

#4)teacher
count=int(input("Enter the number of pupil :"))
sweets=int(input("Enter how many sweets :"))
distribute=sweets//count
sweets_left= sweets%count
print(f"Each pupil will get {distribute} sweets, and will be left with {sweets_left} sweets ")

