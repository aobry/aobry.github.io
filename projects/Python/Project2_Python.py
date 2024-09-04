#Aaron OBryant
#CMIS 102 6982
#July 04, 2022
#This program will compute the cost of house cleaning services
def main():
    #Greetings
    print("Thank you for choosing CleanSweepz!")

    #Input Room information
    print("How many bedrooms do you have?:\t")
    BedRoom = int(input())
    print("How many bathrooms do you have?:\t")
    BathRoom = int(input())

    RoomNumber = BathRoom + BedRoom

    #Input Cleaning services
    print("Please enter 1 for 'Yes' or 0 for 'No' if you would like the following services.")
    print("Would you like your windows cleaned?\t")
    WindowClean = int(input())
    print("Would you like your floors cleaned?\t")
    FloorClean = int(input())
    print("Would you like your furniture to dusted?:\t")
    DustClean = int(input())

    

    #Housing size surcharges
    if (RoomNumber <= 3):
        HouseCost = 0
    elif (RoomNumber == 4):
        HouseCost = 8
    elif (RoomNumber >= 5):
        HouseCost = 12
        
    #Variables
    WindowClean = 15
    FloorClean = 20
    DustClean = 30
    FinalCost = HouseCost + WindowClean + FloorClean +DustClean
   
    

    #Output
    print("Your total will be:", FinalCost)

    

    #Farewell
    print("Thank you for choosing CleanSweepz!")
#Execute
main()


    
