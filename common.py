""" Common module
implement commonly used functions here
"""

import random
import ui
import datetime
import data_manager

def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    valid_id = False
    while valid_id==False:
        generated = ''

        sequence=''
        list_of_chars = ['1','1','2','2','3','3','4','4',]
        while len(list_of_chars)>0:
            
            s= (random.randrange(0,len(list_of_chars)))
            a=''.join(list_of_chars[s])
            sequence += a
            list_of_chars.pop(s)

        
        random_id=""
        for i in range(len(sequence)):
            if sequence[i] == '1':
                
                random_id += str(random.randrange(0,10))
            elif sequence[i] == '2':
                random_id += chr(random.randrange(65,91))
            elif sequence[i] == '3':
                random_id += chr(random.randrange(97,123))
            else:
                random_id += chr(random.randrange(33,48))
    
        if random_id not in table:
            generated=random_id
            valid_id=True


    return generated

def add(table,list_of_titles):
    new_id=generate_random(table)
    new_item = (ui.get_inputs(list_of_titles[1:], "Please enter the datas"))
    new_item.insert(0,new_id)
    
    table.append(new_item)

    return table

def remove(table, id_):
    delete_line=''
    for i in range(len(table)):
        
        if table[i][0]==id_:
            delete_line=i
    try:
        table.pop(int(delete_line))
    except:
        ui.print_error_message("There is no record with that ID.")
    return table

def update(table, id_, list_of_titles):
    new_data=[]
    for i in range(len(table)):
        
        if table[i][0]==id_:
               
            new_data.append(ui.get_inputs(list_of_titles[1:],"Update records."))
            for j in range(len(new_data[0])):
                table[i][j+1] = new_data[0][j]

    return table


def check_date_between(end_date, start_date, this_date):
    if datetime.date(this_date[0],this_date[1],this_date[2])<datetime.date(end_date[0],end_date[1],end_date[2]) and datetime.date(this_date[0],this_date[1],this_date[2])>datetime.date(start_date[0],start_date[1],start_date[2]):
        return True
    else:
        return False

def check_valid_date(start_date,end_date):
    try:
        if datetime.date(int(end_date[0]),int(end_date[1]),int(end_date[2]))-datetime.date(int(start_date[0]),int(start_date[1]),int(start_date[2]))>datetime.timedelta(0):
            return True
    except:
        return False

def check_table(table,list_of_types):

    for i in range(len(table)):
        for j in range(len(table[i])):
            try:
                
                if list_of_types[j]==1:
                    table[i][j] =  str(table[i][j])
                if list_of_types[j]==2:
                    table[i][j] =  int(table[i][j])
            except:
                
                return False    
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] =  str(table[i][j])     
    return True

def check_data_and_write_to_file(table,LIST_OF_TYPES, CSV_FILE, message):
    if check_table(table, LIST_OF_TYPES):
        data_manager.write_table_to_file(CSV_FILE,table)
        ui.print_progress("Record {} {}".format(message, CSV_FILE))
    else:
        ui.print_error_message("Invalid data \n Record not saved.")
    