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