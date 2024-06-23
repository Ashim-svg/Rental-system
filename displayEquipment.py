from tabulate import tabulate
# display function is herae to display the equipments data in tabulate format
def displayequipment(equipment_data):
    headers = ["ID", "Name", "Brand", "Price", "Quantity"]
    data = []
    for id, equipment in equipment_data.items():
        data.append([id, equipment['name'], equipment['brand'], equipment['price'], equipment['quantity']])
    
    table = tabulate(data, headers=headers, tablefmt="grid")
    print("\n#======================= Available Stocks of Equipments ===========================#")
    print(table)
    print("#==================================================================================#\n")
    