""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

CSV_FILE = "store/games.csv"
LIST_OF_TITLE = ["ID", "Title", "Manufacturer", "Price", "In Stock"]
TABLE = data_manager.get_table_from_file(CSV_FILE)
DICT_OF_TYPES = {1:'str',2:'int'}
LIST_OF_TYPES =[1, 1, 1, 2, 2]

def choose(menu):
    inputs = ui.get_inputs(["Please enter a number "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file(CSV_FILE))
    elif option == "2":
        table=add(data_manager.get_table_from_file(CSV_FILE))
        common.check_data_and_write_to_file(table,LIST_OF_TYPES, CSV_FILE, "saved to")
    elif option == "3":
        id_get = ui.get_inputs([LIST_OF_TITLE[0]],"Enter the ID of the item you want to delete: ")
        id_=''.join(id_get)

        table = remove(data_manager.get_table_from_file(CSV_FILE),id_)
        common.check_data_and_write_to_file(table,LIST_OF_TYPES, CSV_FILE, "removed from")
        
        #if common.check_table(table, LIST_OF_TYPES):
        #    data_manager.write_table_to_file(CSV_FILE,table)
        #else:
        #    ui.print_error_message("Invalid data \n Record not saved.")
    elif option == "4":
        id_get = ui.get_inputs([LIST_OF_TITLE[0]],"Enter the ID of the item you want to modify: ")
        id_=''.join(id_get)
        table = update(data_manager.get_table_from_file(CSV_FILE),id_)
        common.check_data_and_write_to_file(table,LIST_OF_TYPES, CSV_FILE, "updated in")
    elif option == "5":
        
        ui.print_result(get_counts_by_manufacturers(data_manager.get_table_from_file(CSV_FILE)), "count")
    elif option == "6":
        manufacturer = ''.join(ui.get_inputs(["Manufacturer: "], "Average amount of games in stock of a given manufacturer."))
        ui.print_result(get_average_by_manufacturer(data_manager.get_table_from_file(CSV_FILE), manufacturer), "Average amount of games in stock by {}".format(manufacturer))
    
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
    return True

def handle_menu():
    options=["Show table",
             "Add to store",
             "Remove from store",
             "Update item",
             "Counts by manufacturers",
             "Average by manufacturer",
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
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    
    table=common.update(table,id_, LIST_OF_TITLE)
    
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    manufacturer_sum = {}
    for i in range(len(table)):
        count= manufacturer_sum.get(table[i][2])
        if count==None:
            manufacturer_sum[table[i][2]] = 1
             
        else:
            manufacturer_sum[table[i][2]] = count+1
    return manufacturer_sum


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    count=0
    sum_games=0
    for i in range(len(table)):
        if table[i][2]==manufacturer:
            sum_games += int(table[i][4])
            count += 1
    try:
        avg = float(sum_games)/count        
    except:
        avg=0
    return avg
