#Instrument booking system

instruments = []

def create_user ():
    print ("Create new Username")
    ID = (input("Create New ID"))
    print ("New User added into system")

def create_instrument():
    print("\n--- Add New Instrument ---")
    name = input("Enter the name of the instrument: ")
    type_ = input("Enter the type of the instrument (e.g., Guitar, Piano): ")
    while True:
        try:
            available_quantity = int(input("Enter the available quantity: "))
            break
        except ValueError:
            print("Please enter a valid number for the quantity.")
    

    instrument = {'id': len(instruments) + 1, 'name': name, 'type': type_, 'available_quantity': available_quantity}
    instruments.append(instrument)
    print(f"Instrument '{name}' added successfully.")


def read_instruments():
    print("\n--- View All Instruments ---")
    if instruments:
        for instrument in instruments:
            print(f"ID: {instrument['id']}, Name: {instrument['name']}, Type: {instrument['type']}, Available Quantity: {instrument['available_quantity']}")
    else:
        print("No instruments available.")

def update_instrument():
    print("\n--- Update Instrument ---")
    try:
        instrument_id = int(input("Enter the ID of the instrument to update: "))
        instrument = next((instr for instr in instruments if instr['id'] == instrument_id), None)
        
        if instrument:
            name = input(f"Enter new name (leave blank to keep '{instrument['name']}'): ")
            type_ = input(f"Enter new type (leave blank to keep '{instrument['type']}'): ")
            available_quantity = input(f"Enter new available quantity (leave blank to keep '{instrument['available_quantity']}'): ")

            if name:
                instrument['name'] = name
            if type_:
                instrument['type'] = type_
            if available_quantity:
                instrument['available_quantity'] = int(available_quantity)
            
            print(f"Instrument with ID {instrument_id} updated successfully.")
        else:
            print("Instrument not found.")
    except ValueError:
        print("Invalid ID. Please enter a valid number.")

def delete_instrument():
    print("\n--- Delete Instrument ---")
    try:
        instrument_id = int(input("Enter the ID of the instrument to delete: "))
        global instruments
        instruments = [instr for instr in instruments if instr['id'] != instrument_id]
        print(f"Instrument with ID {instrument_id} deleted successfully.")
    except ValueError:
        print("Invalid ID. Please enter a valid number.")

def menu():
    while True:
        print("\nInstrument Rental System")
        print("1. Create user")
        print("2. Add Instrument")
        print("3. Read All Instruments")
        print("4. Update Instrument")
        print("5. Delete Instrument")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_user ()
        elif choice == "2":
            create_instrument()
        elif choice == "3":
            read_instruments()
        elif choice == "4":
            update_instrument()
        elif choice == "5":
            delete_instrument()
        elif choice == "6":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the system
if __name__ == "__main__":
    menu()
