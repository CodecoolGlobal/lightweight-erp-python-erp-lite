""" Common module
implement commonly used functions here
"""

import random
import ui

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

        print (sequence)
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
    print (new_id)
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