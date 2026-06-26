print("Contact Book")
contacts = {"Organizer": "9876543210"}
used_numbers = {"9876543210"} 
new_name = input("Enter new contact name: ")
new_number = input("Enter 10-digit phone number: ")
if new_number in used_numbers:
    print("Error: This phone number is already registered!")
else:
    contacts[new_name] = new_number
    used_numbers.add(new_number)
    print(f"Added {new_name} successfully.")
print("\nCurrent Contacts Directory:")
print(contacts)