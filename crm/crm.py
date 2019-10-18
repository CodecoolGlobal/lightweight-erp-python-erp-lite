""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

file_name = 'crm/customers.csv'
TABLE = data_manager.get_table_from_file(file_name)
LIST_OF_TITLES = [ "ID", "Name","Email adress", "Subscribed"]
OPTION = ['0', '1', '2', '3', '4', '5', '6']

title = "HR menu:"
options = ["Show table",
           "Add record",
           "Remove record",
           "Update data",
           "Longest ID",
           "Get subscriber email"]

exit_message = "Back to main menu"

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    while True:
        ui.print_menu(title, options, exit_message)
        try:
            choose()
        except ValueError:
            break
        except KeyError:
            ui.print_error_message('There is no such option')
    # your code

def choose():
    inputs = ui.get_inputs(['Enter a number: '], '')
    option = inputs[0]
    if option == "1":
        show_table(TABLE)
    elif option == "2":
        add(TABLE)
    elif option == "3":
        id_get = ui.get_inputs([LIST_OF_TITLES[0]],"Enter the ID of the item you want to delete: ")
        id_=''.join(id_get)

        remove(TABLE,id_)
        data_manager.write_table_to_file(file_name, TABLE)
    elif option == "4":
        id_get = ui.get_inputs([LIST_OF_TITLES[0]],"Enter the ID of the item you want to modify: ")
        id_=''.join(id_get)
        table = update(TABLE,id_)
        data_manager.write_table_to_file(file_name, table)
    elif option == "5":
        ui.print_result (get_longest_name_id(TABLE), "The longest name is:") 
    elif option == "6":
        ui.print_result(get_subscribed_emails(TABLE), "The names and emails of the subscribed customers:")
    elif option == '0':
        raise ValueError
    while option not in OPTION:
        raise KeyError

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    ui.print_table(table, LIST_OF_TITLES)
    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    table=common.add(table, LIST_OF_TITLES)
    # your code

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
    # your code

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
    table=common.update(table,id_, LIST_OF_TITLES)
    # your code

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    longest_name = len("a")
    names = []
    ids = []
    for i in range(len(table)):
        if len(table[i][1]) > longest_name:
            longest_name_index = i
            longest_name = len(table[i][1])
            names = []
            ids = []
            names.append(table[i][1])
            ids.append(table[i][0])
        elif len(table[i][1]) == longest_name:
            names.append(table[i][1])
            ids.append(table[i][0])
    result = ""
    for i in range(len(ids)):
        result = ids[0]
        if ids[i]>result:
            result = ids[i]
    
    return result


    
    # your code


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """
    customers = []
    for row in table:
        customer = ""
        if row [3] == "1":
            customer = ";".join([row[2],row[1]])
            customers.append(customer)
    return customers
    # your code
