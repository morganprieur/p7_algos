
import csv


# with open('eggs.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))
# Spam, Spam, Spam, Spam, Spam, Baked Beans
# Spam, Lovely Spam, Wonderful Spam


def read_the_infos(): 
    """ Read the infos file to get the actions, their prices and their benefits. 
        Returns:
            list: the actions from the file. 
    """ 
    registered_actions = [] 
    with open('data/donnees_par_action.csv', 'r') as file: 
        reader = csv.reader(file, delimiter='\t') 
        for row in reader: 
            registered_actions.append(row) 
    return registered_actions 


registered_actions = read_the_infos() 
print(registered_actions) 

