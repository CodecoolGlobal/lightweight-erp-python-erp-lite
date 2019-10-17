""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

CSV_FILE = "accounting/items.csv"
LIST_OF_TITLE = ["ID", "Month", "Day", "Year", "Type", "Amount"]
TABLE = data_manager.get_table_from_file(CSV_FILE)
DICT_OF_TYPES = {1:'str',2:'int'}
LIST_OF_TYPES =[1, 2, 2, 2, 1, 2]

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
                
    elif option == "4":
        id_get = ui.get_inputs([LIST_OF_TITLE[0]],"Enter the ID of the item you want to modify: ")
        id_=''.join(id_get)
        table = update(data_manager.get_table_from_file(CSV_FILE),id_)
        common.check_data_and_write_to_file(table,LIST_OF_TYPES, CSV_FILE, "updated in")
    elif option == "5":
        
        ui.print_result(which_year_max(data_manager.get_table_from_file(CSV_FILE)), "max year")
    elif option == "6":
        try:
            year =int(''.join(ui.get_inputs(["Year: "], "Available items in a given year.")))
            ui.print_result(avg_amount(data_manager.get_table_from_file(CSV_FILE), year), "Average profit in {}".format(year))
    
        except:
            ui.print_error_message("Thats not a number.")
        
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
    return True

def handle_menu():
    options=["Show table",
             "Add item",
             "Remove item",
             "Update item",
             "which_year_max",
             "avg_amount",
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

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    profit={}
    for i in range(len(table)):
        count = profit.get(table[i][3])
        if count==None:
            if table[i][4]=='in':
                profit[table[i][3]]=0
                profit[table[i][3]] = profit[table[i][3]]+int(table[i][5])

            else :
                profit[table[i][3]]=0
                profit[table[i][3]] = profit[table[i][3]]-int(table[i][5])

        else:
            if table[i][4]=='in':
                profit[table[i][3]] = profit[table[i][3]]+int(table[i][5])

            else:
                profit[table[i][3]] = profit[table[i][3]]-int(table[i][5])

    max_profit=-99999999999
    result=''
    for key, value in profit.items():
        if value>max_profit:
            max_profit=value
            result=int(key)

    return result

def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    profit={}
    
    for i in range(len(table)):
        count = profit.get(table[i][3])
        if count==None:

            if table[i][4]=='in':
                profit[table[i][3]]=0
                profit[table[i][3]] = profit[table[i][3]]+int(table[i][5])

            else :
                profit[table[i][3]]=0
                profit[table[i][3]] = profit[table[i][3]]-int(table[i][5])

        else:
            if table[i][4]=='in':
                profit[table[i][3]] = profit[table[i][3]]+int(table[i][5])

            else:
                profit[table[i][3]] = profit[table[i][3]]-int(table[i][5])
    count_each={}

    for i in range(len(table)):
        count = count_each.get(table[i][3])
        if count==None:
            count_each[table[i][3]]=1
        else:
            count_each[table[i][3]]=count+1

    
    try:
        avg = float(profit.get(str(year)))/count_each.get(str(year))
        
    except:
        avg=0
    
    return avg