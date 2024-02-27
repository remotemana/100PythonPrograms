# Program 005: File Data Processor

def read_and_process_file(filename):
    with open(filename, 'r') as file:
        names = file.readlines()
        names = [name.strip() for name in names]  # Remove any trailing newline characters
        
    print("Names in uppercase:")
    for name in names:
        print(name.upper())
        
    print(f"\nTotal number of names: {len(names)}")

def add_name_to_file(filename):
    new_name = input("Enter a new name to add: ").strip()
    with open(filename, 'a') as file:
        file.write(f"{new_name}\n")
    print(f"{new_name} has been added to the file.")
    
# Main program starts here
filename = 'names.txt'

read_and_process_file(filename)

# Ask if the user wants to add a new name
if input("Would you like to add a new name? (yes/no): ").lower() == 'yes':
    add_name_to_file(filename)
    # Re-process the file to show the updated list
    read_and_process_file(filename)
