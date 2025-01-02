#question number 1
def base_number(number):
    binary=0
    place=1
    for i in range(32):  
        remainder = number % 2
        binary += remainder * place
        place *= 10
        number //= 2
        if number == 0: 
            return binary
    return binary
print(base_number(45))

#question number 2

def prime_factors(number):
    factors =[]
    for i in range(1,number+1):
        if number % i ==0:
         factors.append(i)
    return factors
print(prime_factors(10))


#question number 3
def prime_factors(number):
    factors =[]
    for i in range(1,number+1):
        if number % i ==0:
             factors.append(i)
    return factors
print(prime_factors(20))


#question number 4
def identifying_prime(number):
    if number<=1:
        return False
    for number in range(2, number+1):
        return True
    for divisior in range(2,number):
        if number% divisior ==0:
            return False
        
print(identifying_prime(20))

#question number 5
def encrypt_message(message):
    encrypted = ""
    for char in message:
        if char != " ":
            encrypted = char + encrypted
    return encrypted
message = "BLACK PINK"
encrypted = encrypt_message(message)
print(encrypted)
