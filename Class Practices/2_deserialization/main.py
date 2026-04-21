from file_handler import FileHandler
from item import Item

filename = "inventory.csv"
inventory_file = FileHandler(filename) # Create an object 
rows = inventory_file.read() # Use read method for the previously created object
print(f'#####Start: {filename}####')

for row in rows: 
    item = Item.deserialize(row)
    item.display_price()
print(f'#####END: {filename}####')