from dataclasses import dataclass # comes from the standard library module dataclasses. Have to be imported 

@dataclass 
class Item: 
    SEPARATOR = ","
    name: str
    value: float
    category: str
    weight: float 

    @staticmethod
    def deseralize(row: str) -> 'Item': 
        columns = row.split(Item.SEPARATOR) #Comma separated values
        item= Item(
            columns[0], #name
            columns[1], #value
            columns[2], #category
            columns[3], #weight
        )
        return item

    def display_price(self):
        print(f'{self.name} costs {self.value} euro.')
        return None

    def set_value(self, new_value: float): 
        if new_value < 0:
            print("Value cannot be negative.")
        else:
            self.value = new_value
    def serialize(self): 
        columns: list[str] = []
        columns.append(self.name)
        columns.append(str(self.value))
        columns.append(self.category)
        columns.append(str(self.weight))
        row = ','.join(columns)
        return row
