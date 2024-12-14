#1)
name=str(input("Enter your name :"))
if name== "" :
    print('"Hello,Stranger!"')
else:
    print("Hello,",name,"Good to meet you!")


#2)
psw1=(input("Enter the password : "))
psw2=(input("Enter the password again : "))
if psw1==psw2:
    print("Password Set")
if psw1!= psw2:
    print("Error occured")

#3)
psw = input("Enter the password: ")
if len(psw)<8 or len(psw)>12:
    print("Password must be between 8 to 12 characters long.")
else:
    check_psw = input("Confirm the password: ")

    if psw == check_psw:
        print("Password Set")
    else:
        print("Sorry! The password did not match")

#4)list psw
bad_passwords= ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
psw=input("Enter a password :")
if psw== bad_passwords :
    print("The given password could not be set")
else:
    print("password set")

#5) don't know

#6)
print("Multiplication table of 7 :")
for i in range(13):
    print(7,"*",i,"=",7*i)

#7)
number=int(input("Enter the number :"))
print("The multiplication table of",number)
if number>=0 and number<=12 :
    for i in range(11):
        print(number,"*",i,"=",number*i)
else:
    print("number not within the range")

#8)backword table
number=int(input("Enter the number :"))
print("The multiplication table of",number)
if number>=0 and number<=12 :
    for i in range(11):
        print(number,"*",i,"=",number*i)
elif number<=0 and number<=12 :
    for i in range(12,1,-1):
        print(number,"*",i,"=",number*i)
else:
    print("number not within the range")