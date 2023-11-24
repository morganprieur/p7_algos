
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
        fileReader = csv.reader(file, delimiter='\t') 
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


# def define_basket_brute_force(list_to_chose, max_amount): 
def define_basket_brute_force(list_to_chose, max_amount): 
    basket = [] 
    total_amount = 0 
    for i in range(len(list_to_chose)): 
        print(i) 
        print(list_to_chose[i]) 
        total_amount += int(list_to_chose[i][1]) 
        if total_amount <= max_amount: 
            basket.append(list_to_chose[i]) 
            # yield list_to_chose[i] 
        else: 
            total_amount -= int(list_to_chose[i][1]) 
            for j in range(len(list_to_chose), i + 1):
                print(j) 
                print(list_to_chose[j]) 
                total_amount += int(list_to_chose[j][1]) 

    return (basket, total_amount) 


registered_actions = read_the_infos() 
# print('\n') 
# print(registered_actions) 
formated_actions = formate_the_infos(registered_actions) 
# print('\n') 
# print(formated_actions) 
sorted_list = sort_the_infos(formated_actions, key=lambda x: x[2], reverse=True) 
# sorted_list = sort_the_infos(registered_actions, key=itemgetter(1), reverse=False) 
# print('\n') 
# print(sorted_list) 
# basket = define_basket_firsts(sorted_list, 500)[0] 
# amount = define_basket_firsts(sorted_list, 500)[1] 
basket = define_basket_brute_force(sorted_list, 500)[0] 
amount = define_basket_brute_force(sorted_list, 500)[1] 
# print('\n') 
print(basket) 
print(amount) 


