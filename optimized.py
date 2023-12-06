
import sys 
import csv 
from itertools import combinations 


def main(): 
    # print('main') 

    registered_list = read_the_infos() 
    formated_list = formate_the_infos(registered_list) 
    calculated_list = calculate_the_benefit(formated_list) 
    # lambda column: column[1] 
    # sorted_benef_list = sort_the_infos(calculated_list, key=lambda x: x[3], reverse=True) 
    # sorted_benef_list = sort_the_infos(calculated_list, key=lambda x: x[1], reverse=True) 
    sorted_benef_list = sort_the_infos(calculated_list, key=column_to_sort, reverse=True) 
    print('\nsorted_benef_list : ', sorted_benef_list) 
    optimized_basket = make_baskets(sorted_benef_list, 500) 
    print('\n', optimized_basket) 


def read_the_infos(): 
    """ Reads the infos file to get the actions, their prices 
            and their benefits. 
            Suppresses the first line from the result. 
        Returns:
            list: the formated actions from the file. 
    """ 
    registered_list = [] 
    with open(f'data/{sys.argv[1]}.csv', 'r') as file: 
        fileReader = csv.reader(file, delimiter=',') 
        for row in fileReader: 
            registered_list.append(row) 
        registered_list.pop(0) 
    return registered_list 


def formate_the_infos(list_to_formate): 
    """ From the given list, adds zeros up to width of 3 to the "bénéfice" column. 
        Returns:
            list: the formated actions. 
    """ 
    formated_list = [] 
    for new_row in list_to_formate: 
        # new_benef = new_row.pop(2) 
        # new_row.append(new_benef.zfill(3)) 
        new_cost = new_row.pop(1) 
        new_row.insert(1, new_cost.zfill(3)) 
        # new_row.append(new_cost.zfill(3)) 
        # new_cost.zfill(3) 
        # print('\nnew_cost : ', new_cost) 
        formated_list.append(new_row) 
    # print('\nformated_list : ', formated_list) 
    return formated_list 


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
        calculated_benefit = (float(line[1]) * float(line[2][:-1]) / 100) 
        line.append(round(calculated_benefit, 2)) 
        calculated_list.append(line) 

    return calculated_list 


def column_to_sort(share): 
    return share[3] 


def sort_the_infos(list_to_sort, key, reverse): 
    """ Sort the infos from a list on the benefit amount column. 
        params: 
            list_to_sort (list): the list to sort. 
            column (str): the column to sort the list on. 
            reverse (bool): ascendant or descendant. 
        return :
            sorted_benef_list: the new sorted list. 
    """ 
    sorted_benef_list = sorted(list_to_sort, key=column_to_sort, reverse=True) 
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
        if float(s[1]) <= float(0): 
            continue 
        purchase += round(float(s[1]), 2) 
        if purchase > max_purchase: 
            purchase -= round(float(s[1]), 2) 
        else: 
            # print(f'\npurchase OP126 : {round(purchase, 2)}') 
            basket.append(s) 
            basket_benefit += round(float(s[3]), 2) 

    if purchase > total_purchase: 
        total_purchase = round(purchase, 2) 

    if basket_benefit > best_benefit: 
        best_benefit = basket_benefit 
        best_basket = basket 
        # print(f'\nbest_benefit OP135 : {round(float(best_benefit), 2)}') 

    with open(f'data/{sys.argv[1]}-export.csv', 'a', encoding='utf-8') as csvfile: 
        csv_writer = csv.writer(csvfile) 
        # adding header 
        file_name = [f'{sys.argv[1]}-export.csv'] 
        headerList = ['name', 'price', 'profit'] 
        cost = [f'coût total : {round(total_purchase, 2)}'] 
        profit = [f'profit total : {round(best_benefit, 2)}'] 
        csv_writer.writerow(file_name) 
        csv_writer.writerow(headerList) 
        csv_writer.writerows(basket) 
        csv_writer.writerow(cost) 
        csv_writer.writerow(profit) 


    return (best_basket, total_purchase, round(best_benefit, 2)) 


if __name__ == '__main__': 
    # print('name') 
    main() 

