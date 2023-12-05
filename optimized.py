
import csv 
from itertools import combinations 


def main(): 
    # print('main') 

    registered_shares = read_the_infos() 
    formated_list = formate_the_infos(registered_shares) 
    calculated_list = calculate_the_benefit(formated_list) 
    sorted_benef_list = sort_the_infos(calculated_list, key=lambda x: x[3], reverse=True) 
    optimized_basket = make_baskets(sorted_benef_list, 500) 
    print('\n', optimized_basket) 
    # print('\n', sorted_benef_list) 


def read_the_infos(): 
    """ Reads the infos file to get the actions, their prices 
            and their benefits. 
            Suppresses the first line from the result. 
        Returns:
            list: the formated actions from the file. 
    """ 
    registered_shares = [] 
    with open('data/donnees_par_action.csv', 'r') as file: 
        fileReader = csv.reader(file, delimiter=',') 
        for row in fileReader: 
            registered_shares.append(row) 
        registered_shares.pop(0) 
    return registered_shares 


def formate_the_infos(list_to_formate): 
    """ From the given list, adds zeros up to width of 3 to the "bénéfice" column. 
        Returns:
            list: the formated actions. 
    """ 
    formated_shares = [] 
    for new_row in list_to_formate: 
        new_benef = new_row.pop(2) 
        new_row.append(new_benef.zfill(3)) 
        formated_shares.append(new_row) 
    return formated_shares 


def calculate_the_benefit(list_to_calculate): 
    """ Calculates the price * the benefit % for each action. 
        Args:
            list_to_calculate (list): the list to calculate. 
        Returns:
            list: the list with the calculated benefit. 
    """ 
    calculated_list = [] 
    calculated_benefit = 0 

    for line in list_to_calculate: 
        calculated_benefit = (float(line[1]) * float(line[2][:2]) / 100) 
        line.append(calculated_benefit) 
        calculated_list.append(line) 

    return calculated_list 


def sort_the_infos(list_to_sort, key, reverse): 
    """ Sort the infos from a list on the benefit amount column. 
        params: 
            list_to_sort (list): the list to sort. 
            column (str): the column to sort the list on. 
            reverse (bool): ascendant or descendant. 
        return :
            sorted_benef_list: the new sorted list. 
    """ 
    sorted_benef_list = sorted(list_to_sort, key=lambda x: x[3], reverse=True) 
    # for line1 in sorted_benef_list: 
    #     print(f'sorted line : {line1}')  # ok 
    return sorted_benef_list 


def make_baskets(sorted_benef_list, max_purchase):
    """ Read the file containing the share's list, 
        set all the pourcentages up to 2 digits, 
        calculate the profit for each share, 
        set all combinations of shares. 
        params: 
            list_to_formate (list): list of shares from file. 
            max_amount (int): the amount constraint of buying shares. 
    """ 
    total_purchase = round(float(0), 2) 
    best_benefit = round(float(0), 2) 
    best_basket = () 

    purchase = round(float(0), 2) 
    basket = [] 
    basket_benefit = round(float(0), 2) 

    for s in sorted_benef_list: 
        print(f'\nmax_purchase OP98 : {max_purchase}') 
        purchase += int(s[1]) 
        if purchase > max_purchase: 
            purchase -= int(s[1]) 
        else: 
            print(f'\npurchase OP103 : {purchase}') 
            basket.append(s) 
            print(f'\nbasket OP105 : {basket}') 
            basket_benefit += round(float(s[3]), 2) 
            print(f'\nbasket_benefit OP107 : {round(float(basket_benefit), 2)}') 

    if purchase > total_purchase: 
        total_purchase = purchase 

    if basket_benefit > best_benefit: 
        best_benefit = basket_benefit 
        best_basket = basket 
        print(f'\nbest_benefit OP115 : {round(float(best_benefit), 2)}') 

    with open('data/combos_opti.csv', 'a', encoding='utf-8') as csvfile: 
        csv_writer = csv.writer(csvfile, delimiter=',') 
        csv_writer.writerow('-  ') 
        csv_writer.writerow(str(purchase)) 
        csv_writer.writerow(str(basket_benefit)) 
        csv_writer.writerows(basket) 


    return (best_basket, total_purchase, round(best_benefit, 2)) 


if __name__ == '__main__': 
    # print('name') 
    main() 

