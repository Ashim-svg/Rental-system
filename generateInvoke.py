import datetime
# Function to generate an invoice
def generateinvoke(customer_name, equipment_list, transaction_type, total_amount):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    invoice_file_name = f"{customer_name}_{transaction_type}_Invoice.txt"
     # Open the invoice file for writing
    with open(invoice_file_name, "w") as file:
        file.write(f"{'='*40} Invoice {'='*40}\n")
        file.write(f"Customer Name: {customer_name}\n")
        file.write(f"Date and Time: {current_time}\n\n")
        file.write("="*80 + "\n")
        file.write(f"{'Equipment':<30}{'Brand':<20}{'Price':<15}{'Quantity':<10}\n")
        file.write("="*80 + "\n")
        for equipment in equipment_list:
            file.write(f"{equipment['name']:<30}{equipment['brand']:<20}{equipment['price']:<15}{equipment['quantity']:<10}\n")
        file.write("="*80 + "\n")
        file.write(f"Total Amount: ${total_amount:.2f}\n")
        file.write("="*80 + "\n")
        file.write("==================================Thank you for using our rental service!=============================")
