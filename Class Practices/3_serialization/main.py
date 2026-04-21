from file_handler import FileHandler
from item import Item

class Main: 
    def __init__(self) -> None: 
        filename = "inventory.csv" 
        inventory_file = FileHandler(filename)
        rows = inventory_file.read()
        print("### inventory ###")
        inventory: list[Item] = []
        for row in rows:
             _item = Item.deserialization(row)
             _item.display_price()
             inventory.append(_item)
        print("### inventory ###")
        feed = input(f"CHange item value (enter 1 - {len(inventory)}): ")
        try: 
             index = int(feed) -1 
             feed = input(f"Set new value for {inventory[index].name}: ")
             inventory[index].set_value(float(feed))
        except Exception: 
             print("Oops, something went wrong.")
        print("Serializing items into rows.")
        print("## Rows ##")
        for _item in inventory:
             row = _item.serialize()
                print(row)
        #print(feed)

        

if __name__ == "__main__": 
        main = Main()