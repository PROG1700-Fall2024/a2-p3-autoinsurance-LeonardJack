#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Firstly i need to take in 3 inputs, gender, age and price
    #use age and gender (with the help of if statements) to calculate the percentage that will be used to aquire their insurance 
    #use my percentage i aquired with my calculation and the price of the car to calculate monthly insurance
    #Print result
    
    invalidInputs = True     #Globals
    insurance = 0

    while invalidInputs:    #while loop to ensure valid inputs
        gender = input("Are you 'Male' or 'Female': ")  #inputs
        age = int(input("Enter your age: "))
        vehiclePrice = float(input("Enter the price of your vehicle when purchased: ")) #^^^^^^
        if gender.lower() == "male" or gender.lower() == "female" and age <= 70 and age >= 15 and vehiclePrice > 0: #determines if inputs are valid
            invalidInputs = False   #if inputs sare valid exits the while loop

    if gender.lower() == "male":    #if statement to determine if user is male
        if age >= 15 and age < 25:          #if statements to catagorize their age and calculate their vehicle price
            insurance = (vehiclePrice * 0.25) / 12
        elif age >=25 and age < 40:
            insurance = (vehiclePrice * 0.17) / 12
        elif age >= 40 and age < 70:
            insurance = (vehiclePrice * 0.10) / 12  #^^^^^^^^^^^^^

    if gender.lower() == "female":      #if statement to determine if user is female
        if age >= 15 and age < 25:      #if statements to catagorize their age and calculate their vehicle price
            insurance = (vehiclePrice * 0.20) / 12
        elif age >=25 and age < 40:
            insurance = (vehiclePrice * 0.15) / 12
        elif age >= 40 and age < 70:
            insurance = (vehiclePrice * 0.10) / 12  #^^^^^^^^^^^^^^^

    print("Your monthly insurance is: ${0:.2f}".format(insurance))  #print statement for the insurance monthly





    # YOUR CODE ENDS HERE

main()