# updating the stocks  after rental and return process
def updateequipmentstock(equipment_data):
    with open("equipment_data.txt", "w") as file:
        for id, equipment in equipment_data.items():
            file.write(f"{equipment['name']}, {equipment['brand']}, {equipment['price']}, {equipment['quantity']}\n")