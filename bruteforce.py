
import csv 
# from operator import itemgetter  # à tester *** 


def read_the_infos(): 
    """ Reads the infos file to get the actions, their prices 
            and their benefits. 
            Suppresses the first line from the result. 
        Returns:
            list: the formated actions from the file. 
    """ 
    registered_actions = [] 
    with open('data/donnees_par_action.csv', 'r') as file: 
        # fileReader = csv.reader(file, delimiter='\t') 
        fileReader = csv.reader(file, delimiter=',') 
        for row in fileReader: 
            registered_actions.append(row) 
        registered_actions.pop(0) 

    return registered_actions 


def formate_the_infos(list_to_formate): 
    """ From the given list, adds zeros up to width of 3 to the "bénéfice" column. 
        Returns:
            list_to_formate: the formated actions. 
    """ 
    formated_actions = [] 
    for new_row in list_to_formate: 
        new_benef = new_row.pop(2) 
        new_row.append(new_benef.zfill(3)) 
        formated_actions.append(new_row) 
    return formated_actions 


def calculate_the_return(list_to_calculate): 
    """ Calculates the amount * the benefit % for each action. 
        Args:
            list_to_calculate (list): the list to calculate. 
        Returns:
            list: the list with the calculated benefit. 
    """ 
    calculated_list = [] 
    calculated_benefit = 0 

    for line in list_to_calculate: 
        calculated_benefit = (int(line[1]) * int(line[2][:2])) / 100 
        line.append(calculated_benefit) 
        calculated_list.append(line) 

    return calculated_list 


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


# def define_basket_firsts(list_to_chose, max_amount): 
#     basket = [] 
#     total_amount = 0 
#     for row in list_to_chose: 
#         total_amount += int(row[1]) 
#         # print(total_amount) 
#         if total_amount <= max_amount: 
#             basket.append(row) 
#         else: 
#             total_amount -= int(row[1]) 
#             # print(total_amount) 
#             break 
#     return (basket, total_amount) 


# partiellement optimisé 
# boucler plusieurs fois jusqu'à avoir fait toutes les combis 
def trying_brute_force(list_to_chose, max_amount): 
    basket = [] 
    total_amount = 0 

    for i in list_to_chose: 
        total_amount += int(i[1]) 
        if total_amount < max_amount: 
            basket.append(i) 
        else: 
            total_amount -= int(i[1]) 
    print(f'\nbasket : {basket}') 
    print(f'\ntotal_amount : {total_amount}') 
    for b in basket: 
        print(f'\nb : {b}') 

    return (basket, max_amount) 


def calculate_benefit_amount(list_to_add): 
    """ Calculates the total benfit of the selected basket. 
        Args:
            list_to_add (list): the list of the selected basket. 
        Returns:
            int: the amount of the benefit for the selected basket. 
    """ 
    benefit_amount = 0 
    for line in list_to_add: 
        benefit_amount += int(line[3]) 
    return benefit_amount 


# def simple_bf(): 
#     ls1 = ['a', 'b', 'c'] 
#     ls2 = ['1', '2', '3'] 
#     res = [] 
#     for i in ls1: 
#         for j in ls2: 
#             res.append(i + j) 
#     return res 
# test = simple_bf() 
# print(test) 


registered_actions = read_the_infos() 
# print('\n') 
# print(registered_actions) 
formated_actions = formate_the_infos(registered_actions) 
# print('\n') 
# print(formated_actions) 
calculated_list = calculate_the_return(formated_actions) 
print('\n') 
print(calculated_list) 
sorted_list = sort_the_infos(calculated_list, key=lambda x: x[2], reverse=True) 
# test = trying_brute_force(sorted_list, 50)
# print('\n')  
# print(test[0]) 
# print(test[1]) 
test_bf = trying_brute_force(sorted_list, 50)
print('\n')  
print(test_bf) 
# sorted_list = sort_the_infos(registered_actions, key=itemgetter(1), reverse=False) 
# print('\n') 
# print(sorted_list) 
total_benef = calculate_benefit_amount(test_bf[0]) 
print('\n') 
print(total_benef) 



