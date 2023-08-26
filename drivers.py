from tabulate import tabulate
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        pass
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        pass
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        pass
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"{self.product} ({self.code}) from {self.country} costs ${self.cost} and we have {self.quantity} in stock."

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data(shoe_list):
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    
    with open('inventory.txt', 'r') as file:
        lines = file.readlines()[1:] # Skip the first line
        for line in lines:
            try:
                country, code, product, cost, quantity = line.strip().split(',')
                shoe_list.append(Shoe(country, code, product, float(cost), int(quantity)))
            except ValueError as e:
                print(f"Error reading line: {line.strip()}. Skipping...")
                continue
    return shoe_list

def capture_shoes(shoe_list):
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country = input("Enter the country of origin: ")
    code = input("Enter the product code: ")
    product = input("Enter the product name: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe added successfully!")


def view_all(shoe_list):
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    headers = ["Country", "Product Code", "Product Name", "Cost", "Quantity"]
    data = [[shoe.country, shoe.code, shoe.product, shoe.get_cost(), shoe.quantity] for shoe in shoe_list]
    print(tabulate(data, headers=headers))

def re_stock(shoe_list):
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
      # Find the shoe with the lowest quantity
    low_quantity_shoe = min(shoe_list, key=lambda x: x.quantity)

    # Prompt the user to add more shoes to the quantity
    print(f"The shoe with the lowest quantity is: {low_quantity_shoe}")
    add_quantity = int(input("Enter the number of shoes to add: "))

    # Update the quantity of the shoe
    low_quantity_shoe.quantity += add_quantity

    # Update the file with the new quantity
    with open("inventory.txt", "r+") as file:
        file_lines = file.readlines()
        file_lines[1 + shoe_list.index(low_quantity_shoe)] = f"{low_quantity_shoe.country},{low_quantity_shoe.code},{low_quantity_shoe.product},{low_quantity_shoe.get_cost()},{low_quantity_shoe.quantity}\n"
        file.seek(0)
        file.writelines(file_lines)
    print("Shoe quantity updated successfully!")


def search_shoe(shoe_list):
    pass
    """This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
   """
     # Prompt the user for the shoe code to search for
    code = input("Enter the shoe code to search for: ")

    # Find the shoe object with the matching code
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe

    # If no matching shoe is found, return None
    return None
    

def value_per_item(shoe_list):
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    print("Shoe Code | Total Value")
    for shoe in shoe_list:
        total_value = shoe.cost * shoe.quantity
        print(f"{shoe.code} | ${total_value}")

def highest_qty(shoe_list):
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    max_quantity = 0
    max_shoe = None
    for shoe in shoe_list:
        if shoe.quantity > max_quantity:
            max_quantity = shoe.quantity
            max_shoe = shoe
    if max_shoe:
        print(f"The shoe with code {max_shoe.code} has the highest quantity of {max_shoe.quantity} and is for sale.")
    else:
        print("There are no shoes available for sale.")
#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

# Define the menu options
MENU_OPTIONS = [
    ("View all shoes", view_all),
    ("Search for a shoe", search_shoe),
    ("Add a new shoe", capture_shoes),
    ("Re-stock a shoe", re_stock),
    ("Calculate value per item", value_per_item),
    ("Find the shoe with the highest quantity", highest_qty),
    ("Exit", None)
]

# Define the initial list of shoes
shoe_list = read_shoes_data(shoe_list)
"""capture_shoes(shoe_list)
view_all(shoe_list)
re_stock(shoe_list)
search_shoe(shoe_list)
value_per_item(shoe_list)"""

# Display the menu and execute the chosen option
while True:
    # Print the menu options
    print("==== Shoe inventory management ====")
    for i, (option, _) in enumerate(MENU_OPTIONS):
        print(f"{i+1}. {option}")
    
    # Get the user's choice
    choice = input("Enter your choice: ")
    
    # Validate the user's choice
    try:
        choice = int(choice)
        if choice < 1 or choice > len(MENU_OPTIONS):
            raise ValueError()
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and", len(MENU_OPTIONS))
        continue
    
    # Execute the chosen function
    option, function = MENU_OPTIONS[choice-1]
    if function is None:
        print("Goodbye!")
        break
    else:
        function(shoe_list)
