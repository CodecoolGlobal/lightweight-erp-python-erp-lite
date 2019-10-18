""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

file_name = 'hr/persons.csv'
TABLE = data_manager.get_table_from_file(file_name)
LIST_OF_TITLES = [ "ID", "Name","Birthyear"]
OPTION = ['0', '1', '2', '3', '4', '5', '6']

title = "HR menu:"
options = ["Show table",
           "Add record",
           "Remove record",
           "Update data",
           "The oldest person",
           "Who is the closest to the average age?"]

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
        ui.print_result(get_oldest_person(TABLE), "The oldest person is:" )
    elif option == "6":
        ui.print_result(get_persons_closest_to_average(TABLE),"Closest to average: ")
    elif option == '0':
        raise ValueError
    while option not in OPTION:
        raise KeyError


def show_table(table):
    ui.print_table(table, LIST_OF_TITLES)

  # """ Args:
   #     table (list): list of lists to be displayed.

   # Returns:
    #    None
    #"""

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    table=common.add(table,LIST_OF_TITLES)
    

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

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    max_age= 2019
    oldpp = []
    for i in range(len(table)):
        if int(table[i][2]) < max_age:
            oldest_index = i
            max_age = int(table[i][2])
            oldpp = []
            oldpp.append(table[i][1])
        elif int(table[i][2]) == max_age:
            oldpp.append(table[i][1])

    return  oldpp
    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
    year_list = []
    for element in table:
        year_list.append(int(element[2]))
    suma = 0
    for element in year_list:
        suma = suma + int(element)
    avarage = float(suma)/int(len(year_list))
    first_person = int(table[0][2])
    list_of_people = []
    for element in table:
        if abs(int(element[2]) - avarage) < abs(first_person - avarage):
            first_person = int(element[2])
            list_of_people[0] = element[1]
        elif abs(int(element[2]) - avarage) == abs(first_person - avarage):
            first_person = int(element[2])
            list_of_people.append(element[1])

    return list_of_people
    

    # your code
