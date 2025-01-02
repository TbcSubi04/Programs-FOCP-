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
countries=input("Enter the country you want to know the capital about : ")
for key,values in countries_with_capitals():
    if countries in countries_with_capitals:
        print(f"The capital of {key} is : {values}")
    else:
        print("Sorry the capital for the country is not stored.")
    

#question number 4

    
