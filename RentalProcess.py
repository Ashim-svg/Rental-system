from displayEquipment import displayequipment
from generateInvoke import generateinvoke
from UpdateStock import updateequipmentstock

# all the renatl process is being carried out
def rentalprocess(equipment_data):
    # Createating  a list to store rented equipment information
    rented_equipment = []
    while True:
        displayequipment(equipment_data)
        try:
            id = int(input("\nEnter the ID of the equipment to rent (0 to finish): "))
            if id == 0:
                if rented_equipment:
                    customer_name = input("Enter customer name: ")
                    number_of_days = input("Days You want to rent: ")
                    total_amount = sum(int(equipment["price"].replace("$", "")) for equipment in rented_equipment)  * (int(number_of_days) / 5)
                     # Calling the function to generate invoice
                    generateinvoke(customer_name, rented_equipment, "Rental", total_amount)
                    print("\nEquipment rented successfully!")
                    updateequipmentstock(equipment_data)
                else:
                    print("No equipment rented.")
                break
            # using if to see equipment ID is valid 
            if id in equipment_data:
                equipment = equipment_data[id]
                quantity = int(input("Enter the quantity to rent: "))
                if 0 < quantity <= equipment["quantity"]:
                    equipment["quantity"] -= quantity
                    rented_equipment.append({
                        "name": equipment["name"],
                        "brand": equipment["brand"],
                        "price": equipment["price"],
                        "quantity": quantity
                    })
                    print("Equipment added to the rental list.")
                else:
                    print("Invalid quantity or equipment not available.")
            else:
                print("Invalid equipment ID.Number should be positive.")
        except ValueError:
            print("Invalid input.")