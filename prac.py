colours = [ "Blue", "Black", "Orange" ]
print("The colour black is in the list : ", "Black" in colours)


stn=int(input("How many students?"))
size=int(input("Required group size?"))
groups= stn//size
students_left= stn%size
print(f"There will be {groups} groups with {students_left} will be left over")

count=int(input("Enter the number of pupil :"))
sweets=int(input("Enter how many sweets :"))
distribute=sweets//count
sweets_left= sweets%count
print(f"Each pupil will get {distribute} sweets, and will be left with {sweets_left} sweets ")
