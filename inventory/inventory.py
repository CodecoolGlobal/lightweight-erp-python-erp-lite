""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

CSV_FILE = "inventory/inventory.csv"
LIST_OF_TITLE = ["ID", "Name", "Manufacturer", "Purchase Year", "Durability"]
TABLE = data_manager.get_table_from_file(CSV_FILE)
DICT_OF_TYPES = {1:'str',2:'int'}
LIST_OF_TYPES =[1, 1, 1, 2, 2]
def choose(menu):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file(CSV_FILE))
    elif option == "2":
        table=add(data_manager.get_table_from_file(CSV_FILE))
        common.check_data_and_write_to_file(table,LIST_OF_TYPES, CSV_FILE,"saved to")
    elif option == "3":
        id_get = ui.get_inputs([LIST_OF_TITLE[0]],"Enter the ID of the item you want to delete: ")
        id_=''.join(id_get)

        table = remove(data_manager.get_table_from_file(CSV_FILE),id_)
        common.check_data_and_write_to_file(table,LIST_OF_TYPES, CSV_FILE, "removed from")

    elif option == "4":
        id_get = ui.get_inputs([LIST_OF_TITLE[0]],"Enter the ID of the item you want to modify: ")
        id_=''.join(id_get)
        table = update(data_manager.get_table_from_file(CSV_FILE),id_)
        common.check_data_and_write_to_file(table,LIST_OF_TYPES, CSV_FILE, "updated in")
    elif option == "5":
        try:
            year =int(''.join(ui.get_inputs(["Year: "], "Available items in a given year.")))
            ui.print_result(get_available_items(data_manager.get_table_from_file(CSV_FILE), year),("Available items in {}".format(year)), LIST_OF_TITLE)
        except:
            ui.print_error_message("Thats not a number.")
        

    elif option == "6":
        ui.print_result(get_average_durability_by_manufacturers(data_manager.get_table_from_file(CSV_FILE)),"Average durability by manufacturers:")
    
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
    return True

def handle_menu():
    options=["Show table",
             "Add to inventory",
             "Remove from inventory",
             "Update item",
             "Available items",
             "Average durability",
                ]

    ui.print_menu("Inventory Menu", options, "Back to Main Menu")


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
       
    menu = True
    while menu:
        
        handle_menu()
        try:
            menu = choose(menu)
        except KeyError as err:
            ui.print_error_message(str(err))
    

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
       
    ui.print_table(table,LIST_OF_TITLE)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    table=common.add(table,LIST_OF_TITLE)
       
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
   
    table= common.remove(table,id_)            
   
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    
    table=common.update(table,id_, LIST_OF_TITLE)
    
    return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code
    available_items = []
    for i in range(len(table)):
        if int(table[i][4])+int(table[i][3])>=int(year):
                try:
                    available_items.append(int(table[i]))
                except:
                    available_items.append(table[i])
    
    
    for i in range(len(available_items)):
        for j in range(len(available_items[i])):
            try:
                available_items[i][j]= int(available_items[i][j])
            except:
                available_items[i][j]= available_items[i][j]

    return available_items


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
    manufacturer_sum = {}
    durability_sum = {}
    avg_durability = {}
    for i in range(len(table)):
        count= manufacturer_sum.get(table[i][2])
        if count==None:
            manufacturer_sum[table[i][2]] = 1
             
        else:
            manufacturer_sum[table[i][2]] = count+1
    for i in range(len(table)):
        count= durability_sum.get(table[i][2])
        if count==None:
            durability_sum[table[i][2]]=table[i][4]
        else:
            durability_sum[table[i][2]]=int(durability_sum.get(table[i][2]))+int(table[i][4])
    for key, value in manufacturer_sum.items():
        avg = float(durability_sum.get(key))/manufacturer_sum.get(key)
        avg_durability[key]=avg
        

    return avg_durability