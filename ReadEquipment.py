#to read the txt file read equipment function is defined
def readequipmentdata():
    equipment_data = {}
    with open("equipment_data.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            name, brand, price, quantity = data
            equipment_data[len(equipment_data) + 1] = {
                "name": name,
                "brand": brand,
                "price": price,
                "quantity": int(quantity)
            }
    return equipment_data