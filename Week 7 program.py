#question number 1
def unique_letters(string):
    return sorted(set(string))

input_string="cheese"
output= unique_letters(input_string)
print(f"The sorted list is {output}")

#question number 2

def sort_letters(para1,para2):
    return sorted((set(para1+para2)))

def both_words(para1,para2):
    return sorted(set(para1) & set(para2))

def either_or_both(para1,para2):
     return sorted(set(para1) & set(para2))

para1="greet"
para2="read"

print(f"Letter that appear atlest one of the two words{sort_letters(para1,para2)}")
print(f"letter that appear in both words{both_words(para1,para2)}")
print(f"Letter that appear in either word,but not in both{para1,para2}")


#question number 3

countries_with_capitals={'Nepal':'Kathmandu','Korea':'Seoul','China':'Beijing','Japan':'Tokyo','France':'Paris'}

country=input("Enter the country you want to know the capital about : ")
if country in countries_with_capitals:
    print(f"The capital of {country} is: {countries_with_capitals[country]}")
else:
    print("Sorry, the capital for the country is not stored.")


#question number 4
def letter_analysis(message):
    count_letters = {}

    for char in message.lower():
        if 'a' <= char <= 'z':
            count_letters[char] = count_letters(char, 0) + 1

    sorted_letters = sorted(count_letters, key=lambda item: item[1], reverse=True)

    for letter, count in sorted_letters[:6]:
        print(f"{letter}: {count} times")


message = "Hello, I hope you have a great day ahead"

letter_analysis(message)
    
