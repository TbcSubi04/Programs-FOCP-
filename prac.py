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


#question 7

def cels_to_fahren(celsius):
    return celsius * (9/5) + 32

def convert_temp(temp):
    if temp[-1].upper() == 'C':
        celsius = float(temp[:-1])
        fahrenheit = cels_to_fahren(celsius)
        return f"{fahrenheit:.2f}F"
    else:
        return "Please enter the temperature followed by 'C'"
    
temperatures= []
for i in range(6):
        temp = input(f"Enter temperature {i+1} in Celsius (e.g., 28C): ")
        
        if temp[-1].upper() == 'C' and temp[:-1]:
            celsius = float(temp[:-1])
            
            fahrenheit = cels_to_fahren(celsius)
            temperatures.append(fahrenheit)
        else:
            print("Not a valid input. Please enter the temperature in C'")

if temperatures: 
    max_temp = max(temperatures) 
    min_temp = min(temperatures) 
    mean_temp= sum(temperatures) / len(temperatures)
    print(f"Maximum temperature: {max_temp:.2f}F") 
    print(f"Minimum temperature: {min_temp:.2f}F") 
    print(f"Mean temperature: {mean_temp:.2f}F") 
else: 
    print("Valid temperatures were not entered")
        