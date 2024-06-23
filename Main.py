import os

from ReadEquipment import readequipmentdata
from RentalProcess import rentalprocess
from ReturnProcess import returnprocess
from displayEquipment import displayequipment
from art import text2art

def main():
    equipment_data = readequipmentdata()
    #infite loop is created here to keep the menur running
    while True:
        print("="*105)
        print(text2art("\n WELCOME 99 STORE"))
        print("="*105)
    
        print("""\n
    =================================================================================================
    *                           99 Rental  Shop                                                     *
    =================================================================================================        
    +                           1. To rent the equipments                                           +
    +                           2. To return the equipment                                          +
    +                           3. Display the details about equipment                              +
    +                           4. Exit the shop                                                    +
    =================================================================================================  
    """)
        #getting user input from the user to display 
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                rentalprocess(equipment_data)
            elif choice == 2:
                returnprocess(equipment_data)
            elif choice == 3:
                displayequipment(equipment_data)
            elif choice == 4:
                print("==================== Visit us Next Time =======================")
                break  
            else:
                print("\n================= Input the desiginated numbers from 1 to 4 #invalid!!! ====================")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
    #calling function start the program
    
