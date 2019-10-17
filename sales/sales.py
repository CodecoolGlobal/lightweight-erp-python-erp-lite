""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


CSV_FILE = "sales/sales.csv"
LIST_OF_TITLE = ["ID", "Title", "Price", "Month", "Day", "Year"]
TABLE = data_manager.get_table_from_file(CSV_FILE)
DICT_OF_TYPES = {1:'str',2:'int'}
LIST_OF_TYPES =[1, 1, 2, 2, 2, 2]
def choose(menu):
    inputs = ui.get_inputs(["Please enter a number: "], "")
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
    elif option == "4":
        id_get = ui.get_inputs([LIST_OF_TITLE[0]],"Enter the ID of the item you want to modify: ")
        id_=''.join(id_get)
        table = update(data_manager.get_table_from_file(CSV_FILE),id_)
        common.check_data_and_write_to_file(table,LIST_OF_TYPES, CSV_FILE, "updated in")
    elif option == "5":
        ui.print_result(get_lowest_price_item_id(data_manager.get_table_from_file(CSV_FILE)), "ID of the item that was sold for the lowest price: ")

    elif option == "6":
        start_date = ui.get_inputs(["Year: ", "Month: ", "Day: "], "Start date: ")
        end_date = ui.get_inputs(["Year: ", "Month: ", "Day: "], "End date: ")
        if common.check_valid_date(start_date,end_date):
            ui.print_result(get_items_sold_between(data_manager.get_table_from_file(CSV_FILE), int(start_date[1]), int(start_date[2]), int(start_date[0]), int(end_date[1]), int(end_date[2]), int(end_date[0])),"Items sold",LIST_OF_TITLE)
        else:
            ui.print_error_message("Invalid date.")
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
    return True

def handle_menu():
    options=["Show table",
             "Add",
             "Remove",
             "Update",
             "Lowest price item id",
             "Items sold between given dates",
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

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    list_of_lowest_price=[]
    min_price=9999999999
    ordered = 'zzzzz'
    id_of_lowest_price=""
        
    for i in range(len(table)):
        if int(table[i][2])<min_price:
            
            min_price=int(table[i][2])
    for i in range(len(table)):
        if int(table[i][2])==min_price:
            list_of_lowest_price.append(table[i])        
          
        
    for i in range(len(list_of_lowest_price)):
        if list_of_lowest_price[i][1]<ordered:
            ordered=list_of_lowest_price[i][1]
            id_of_lowest_price=i
    result=list_of_lowest_price[id_of_lowest_price][0]
    
    return result

    

def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    end_date=[year_to,month_to,day_to]
    start_date=[year_from,month_from,day_from]

    items_sold=[]
    
    for i in range(len(table)):
        if common.check_date_between(end_date,start_date, [int(table[i][5]),int(table[i][3]),int(table[i][4])]):
            items_sold.append(table[i])
            

    for i in range(len(items_sold)):
        for j in range(len(items_sold[i])):
            try:
                items_sold[i][j]= int(items_sold[i][j])
            except:
                items_sold[i][j]= items_sold[i][j]

    return items_sold

