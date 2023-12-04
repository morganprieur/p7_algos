
import csv 
from itertools import combinations 
# import tqdm 
# from operator import itemgetter  # à tester *** 


# ==== # 
def main(): 
    print('main') 

    registered_actions = read_the_infos() 
    # print('\n') 
    # print(registered_actions) 
    formated_actions = formate_the_infos(registered_actions) 
    # print('\n') 
    # print(formated_actions) 
    calculated_list = calculate_the_return(formated_actions) 
    # print('\n') 
    # print(calculated_list) 
    # sorted_list = sort_the_infos(calculated_list, key=lambda x: x[2], reverse=True) 
    # test = trying_brute_force(sorted_list, 50)
    # print('\n')  
    # print(test[0]) 
    # print(test[1]) 
    # test_bf = trying_brute_force(sorted_list, 50) 
    # test_bf = set_combos(sorted_list, 500) 
    test_bf = set_combos(calculated_list, 500) 
    print('\n')  
    print(test_bf) 
    # sorted_list = sort_the_infos(registered_actions, key=itemgetter(1), reverse=False) 
    # print('\n') 
    # print(sorted_list) 
    # total_benef = calculate_benefit_amount(test_bf[0]) 
    # print('\n') 
    # print(total_benef) 
# ==== # 



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
            list: the formated actions. 
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
        calculated_benefit = (float(line[1]) * float(line[2][:2])) / 100 
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


# ==== # 
def set_combos(list_to_chose, max_amount):
    """ 

    Set all possible combinations of shares
        Check if under max possible investment
        Check and get highest profit
        @param shares_list: list of all imported shares data
        @return: most profitable combination (list)
    """ 
    # total_amount = 0 
    profit = 0 
    best_combo = [] 
    # total_benefit = 0 

    # for i in tqdm(range(len(list_to_chose))): 
    for i in range(len(list_to_chose)): 
        # print(f'i : {i}') 
        combos = combinations(list_to_chose, i + 1) 
        print(f'combos : {combos}') 

        for combo in combos: 
            print(f'combo : {combo}') 
            # print(f'profit BF109 : {profit}') 
            total_amount = 0 
            # print(f'total_amount : {total_amount}') 
            total_benefit = 0 
            # print(f'total_benefit : {total_benefit}') 

            with open('data/combos.csv', 'a', encoding='utf-8') as csvfile: 
                csv_writer = csv.writer(csvfile, delimiter=',') 
                csv_writer.writerow('-') 
                csv_writer.writerows(combo) 

            for share in combo: 
                total_amount += float(share[1]) 
                print(f'total_amount : {total_amount}') 
                if total_amount <= max_amount: 
                    total_benefit += share[3] 
                    # print(f'total_benefit : {total_benefit}') 
                else: 
                    total_amount -= float(share[1]) 
                    print(f'total_amount BF128 : {total_amount}') 

                if total_benefit > profit:
                    profit = total_benefit 
                    print(f'profit : {profit}') 
                    best_combo = combo 

    return best_combo 


# def set_combos(shares_list):
#     """ Set all possible combinations of shares
#         Check if under max possible investment
#         Check and get highest profit
#         @param shares_list: list of all imported shares data
#         @return: most profitable combination (list)
#     """ 
#     profit = 0
#     best_combo = []

#     for i in tqdm(range(len(shares_list))):
#         combos = combinations(shares_list, i+1)

#         for combo in combos:
#             total_cost = calc_cost(combo)

#             if total_cost <= MAX_INVEST:
#                 total_profit = calc_profit(combo)

#                 if total_profit > profit:
#                     profit = total_profit
#                     best_combo = combo

#     return best_combo 


# def calc_cost(combo): 
#     """Sum of current share combo prices
#         @param combo: list of current shares combo
#         @return: total cost (float)
#     """
#     prices = []
#     for el in combo:
#         prices.append(el[1]) 
# ==== # 


# partiellement optimisé 
# boucler plusieurs fois jusqu'à avoir fait toutes les combis 
# def trying_brute_force(list_to_chose, max_amount): 
#     baskets = [] 
#     one_basket = [] 
#     total_amount = 0 

#     # payload(list_to_chose, max_amount, total_amount) 

#     for i in range(len(list_to_chose)): 
#         for j in list_to_chose: 
#             total_amount += int(list_to_chose[i][1]) 
#             if total_amount < max_amount: 
#                 one_basket.append(list_to_chose[i]) 
#             else: 
#                 total_amount -= int(list_to_chose[i][1]) 

#         # total_amount += int(list_to_chose[i][1]) 
#         # if total_amount < max_amount: 
#         #     one_basket.append(list_to_chose[i]) 
#         # else: 
#         #     total_amount -= int(list_to_chose[i][1]) 
#         # i += i 
#         baskets.append(one_basket) 

#         for basket in baskets: 
#             print(f'\nbasket : {basket}') 
#             print(f'\ntotal_amount : {total_amount}') 
#             for b in basket: 
#                 print(f'\nb : {b}') 

#     print(f'\nbaskets : {baskets}') 

#     return (one_basket, max_amount) 


# def calculate_benefit_amount(list_to_add): 
# def calculate_benefit_amount(combo): 
def calculate_benefit_amount(share): 
    """ Calculates the total benfit of the selected basket. 
        Args:
            list_to_add (list): the list of the selected basket. 
        Returns:
            int: the amount of the benefit for the selected basket. 
    """ 
    benefit_amount = 0 
    # for share in combo: 
    # print(f'share : {share}') 
    print(f'\nshare : {float(share[3]) }') 
    benefit_amount += float(share[3]) 
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

print('out') 

if __name__ == '__main__': 
    print('name') 
    main() 




