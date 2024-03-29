""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    
    # your goes code
    column_width=[]
    for i in range(len(title_list)):
        column_width.append(len(title_list[i]))

    for i in range(len(title_list)):

        for j in range(len(table)):
            
            if len(str(table[j][i]))>column_width[i]:
                
                column_width[i]=len(str(table[j][i]))

    table_width = 0
    for i in range(len(column_width)):
        table_width += column_width[i]

    print('-'*(table_width+(len(title_list)*4)))
    for j in range(len(title_list)):
            print('| {:^{width1}} |'.format(title_list[j], width1=column_width[j]),end='')
    print()
    print('='*(table_width+(len(title_list)*4)))
    for i in range(len(table)):

        for j in range(len(title_list)):
            print('| {:>{width1}} |'.format(table[i][j], width1=column_width[j]),end='')

        print()
        print('-'*(table_width+(len(title_list)*4)))

    

def print_result(result, label, list_of_title=[]):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(label)
    
    if type(result)==dict:
        for key, value in result.items():
            print('{} :  {}'.format(key, value))
    elif type(result)==list and list_of_title==[]:
        for i in range(len(result)):
            print(result[i])
    elif type(result)==list and list_of_title!=None:
               
        print_table(result, list_of_title)
    
    else:
        print(result)
    print()


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(title)
    print()
    print()
    for i in range(len(list_options)):
        print("{}. {}".format(i+1, list_options[i]))
    print("0. {}".format(exit_message))

    # your code


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)
    print()
    for i in range(len(list_labels)):
        inputs.append(input("{}: ".format(list_labels[i])))
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print()
    print("Error: {}".format(message))
    print()

def print_progress(message):
    print()
    print(message)
    print()