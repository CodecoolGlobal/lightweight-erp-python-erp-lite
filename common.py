""" Common module
implement commonly used functions here
"""

import random


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
