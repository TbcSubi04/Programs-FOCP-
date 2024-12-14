#question number 1

def range(numbers):
    if 0<=numbers<=100:
        return True
    else:
        return False

test_numbers= [-100,0,50,100,200]
for numbers in test_numbers:
  print(f"{numbers} is in range : {range(numbers)}")


#question number 2

def string(p):
    upperCase = 0
    lowerCase = 0

    for char in p:
        if char.isupper():
            upperCase += 1
        elif char.islower():
            lowerCase +=1
    return upperCase, lowerCase

string_check = input("Enter the text you want to count the casing for: ")

Upcase, lowcase = string(string_check)
print(f"String: '{string_check}'")
print(f"Uppercase letters: {Upcase}, Lowercase letters: {lowcase}\n")

#question number 3
name=input("Hello,what is your name :")
greetings=name.capitalize()
print(f"Hello,{greetings}")

#question number 4

def last_character(p):
    if len(p)<=1:          #checks the length of the string
        return p
    else:
        return p[:-1]
remove_last_char= input("Enter any word :")
modified_string= last_character(remove_last_char)
print(f"{remove_last_char} modified : {modified_string}")

#question number 5
def cels_to_fahren(celsius):
    Fahrenheit= celsius*(9/5) +32
    return Fahrenheit

def fahren_to_cels(fahren):
    Celsius= (fahren-32) * 5/9
    return Celsius

temp_in_celsius= float(input("Enter a temperature in celsius :"))
print(f"{temp_in_celsius}C  is equivalent to {cels_to_fahren(temp_in_celsius)}F")

temp_in_Fahren= float(input("Enter a temperature in Fahrenheit :"))
print(f"{temp_in_Fahren}F is equivalent to {fahren_to_cels(temp_in_Fahren)}C")

#question number 6

def cels_to_fahren(celsius):
    return celsius * (9/5) + 32

def convert_temp(temp1):
    if temp1[-1].upper() == 'C':
        celsius = float(temp1[:-1])
        fahrenheit = cels_to_fahren(celsius)
        return f"{fahrenheit:.2f}F"
    else:
        return "Please enter the temperature followed by 'C'"

temp1= input("Enter the temperature in Celsius (e.g., 28C): ")
temp2= convert_temp(temp1)
print(temp2)

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
        

#question number 8

    







