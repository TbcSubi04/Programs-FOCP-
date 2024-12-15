def cels_to_fahren(celsius):
    return celsius * (9/5) + 32

def degrees():
    temperatures = []  
    
    while True:
        temp = input("Enter temperature in Celsius (e.g., 25C) or press Enter to stop: ")
        if temp == "":
            break
        
        if temp[-1].upper() == 'C' and temp[:-1]:
            # to extract the numeric part and convert it into  float
            celsius = float(temp[:-1])
            
            fahrenheit = cels_to_fahren(celsius)
            temperatures.append(fahrenheit)
        else:
            print("Invalid input. Please enter the temperature in the format 'XXC'.")
 
    if temperatures:
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)

        print(f"Maximum Temperature: {max_temp:.2f}F")
        print(f"Minimum Temperature: {min_temp:.2f}F")
        print(f"Mean Temperature: {mean_temp:.2f}F")
    else:
        print("No valid temperatures were entered.")

if __name__ == "__main__":
    degrees()