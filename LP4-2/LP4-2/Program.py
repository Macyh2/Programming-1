weight = int(input("Enter package weight in kilograms:"))
length = int(input("Enter package length in centimeters:"))
width = int(input("Enter package width in centimeters:"))
height = int(input("Enter package height in centimeters:"))

volume = length * height * width

if weight >= 27:
    print("Too Heavy")
    
elif volume >= 1*10**5:
    print ("Too Large")
    
elif weight >= 27 and volume >= 1*10**5:
    print ("Too Heavy & Too Large")
    
input()