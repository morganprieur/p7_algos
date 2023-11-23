
import csv 
# from operator import itemgetter  # à tester *** 


def read_the_infos(): 
    """ Reades the infos file to get the actions, their prices 
            and their benefits. 
            Suppresses the first line from the result. 
            Adds zeros up to width of 3 to the "bénéfice" column. 
        Returns:
            list: the formated actions from the file. 
    """ 
    registered_actions = [] 
    with open('data/donnees_par_action.csv', 'r') as file: 
        fileReader = csv.reader(file, delimiter='\t') 
        new_registered_actions = [] 
        for row in fileReader: 
            registered_actions.append(row) 
        registered_actions.pop(0) 
        for new_row in registered_actions: 
            new_benef = new_row.pop(2) 
            new_row.append(new_benef.zfill(3)) 
            new_registered_actions.append(new_row) 

    return new_registered_actions 


registered_actions = read_the_infos() 


def sort_the_infos(list_to_sort, key, reverse): 
    """ Sort the infos from a list on a specific column. 
        params: 
            list_to_sort (list): the list to sort. 
            column (str): the column to sort the list on. 
            reverse (bool): ascendant or descendant. 
        return :
            sorted_list: the new sorted list. 
    """ 
    sorted_list = sorted(list_to_sort, key=lambda x: x[2], reverse=True) 
    # sorted_list = sorted(list_to_sort, key=itemgetter(1), reverse=False)  
    return sorted_list 


sorted_list = sort_the_infos(registered_actions, key=lambda x: x[2], reverse=True) 
# sorted_list = sort_the_infos(registered_actions, key=itemgetter(1), reverse=False) 
print(sorted_list) 


