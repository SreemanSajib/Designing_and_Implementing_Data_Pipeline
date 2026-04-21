from file_handler import FileHandler

filename = "inventory.csv"
inventory_file = FileHandler(filename) # Create an object 
rows = inventory_file.read() # Use read method for the previously created object
print(f'#####Start: {filename}####')

for row in rows: 
    print(row)

print(f'#####END: {filename}####')