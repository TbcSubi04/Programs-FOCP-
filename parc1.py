countries_with_capitals={'Nepal':'Kathmandu','Korea':'Seoul','China':'Beijing','Japan':'Tokyo','France':'Paris'}

country=input("Enter the country you want to know the capital about : ")
if country in countries_with_capitals:
    print(f"The capital of {country} is: {countries_with_capitals[country]}")
else:
    print("Sorry, the capital for the country is not stored.")



