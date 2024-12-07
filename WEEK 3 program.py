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
#psw=str(input("Enter the password :"))
#if len(psw)>=8 and (psw)<=12 :
 #   print("Password set")
#else:
 #   print("Password not set according to the instructions")

#4)list psw
bad_passwords= ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
psw=input("Enter a password")
if psw in bad_passwords :
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
num=int(input("Enter a number :"))
print("The multiplication table of",num)
if num<=0 and num<=12 :
    for i in range(12,1,-1):
        print(num,"*",i,"=",num*i)