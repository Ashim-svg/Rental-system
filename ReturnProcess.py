from displayEquipment import displayequipment
from generateInvoke import generateinvoke
from UpdateStock import updateequipmentstock

#whole return process is being carried out 
def returnprocess(equipment_data):
    displayequipment(equipment_data)
    try:
        id = int(input("\nEnter the ID of the equipment to return: "))
        if id in equipment_data:
            equipment = equipment_data[id]
            quantity = int(input("Enter the quantity to return: "))
            datetaken = int(input("Days Taken: "))
            
            # Calculate rental duration in days
            rental_duration = 0
            
            # Check if the return is late
            is_late_return = input("Is the return late? (y/n): ").lower() == "y"
            if is_late_return:
                late_days = int(input("Enter the number of days late: "))
                rental_duration += (datetaken / 5)
                fine = 10 * late_days  # Apply fine of $10 per day
            else:
                fine = 0
            
            equipment["quantity"] += quantity
            updateequipmentstock(equipment_data)
            returned_equipment = [{
                "name": equipment["name"],
                "brand": equipment["brand"],
                "price": equipment["price"],
                "quantity": quantity
            }]
            total_amount = (int(equipment["price"].replace("$", "")) * rental_duration )+ fine
            generateinvoke(input("Enter customer name: "), returned_equipment, "Return", total_amount)
            print("\nEquipment returned successfully!")
        else:
            print("Invalid equipment ID.")
    except ValueError:
        print("Invalid input.")