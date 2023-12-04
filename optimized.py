
import csv 
from itertools import combinations 


def main(): 
    print('main') 

    registered_shares = read_the_infos() 
    formated_list = formate_the_infos(registered_shares) 
    calculated_list = calculate_the_return(formated_list) 
    sorted_list = sort_the_infos(calculated_list, key=lambda x: x[2], reverse=True) 
    # optimized_basket = define_basket(sorted_list, 500) 
    optimized_basket = make_combos(sorted_list, 500) 
    print(optimized_basket) 


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
    for line1 in sorted_list: 
        print(f'line1 : {line1}') 
    return sorted_list 


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
    print(f'formated_shares OP59 : {formated_shares}') 
    return formated_shares 


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
        print(f'line2 : {line}') 
        print(f'line2[2] : {line[2]}') 
        calculated_benefit = (round(float(line[1]), 2) * round(float(line[2][:2]), 2) / 100) 
        line.append(calculated_benefit) 
        calculated_list.append(line) 

    return calculated_list 


def make_combos(sorted_list, max_purchase):
    """ Read the file containing the share's list, 
        set all the pourcentages up to 2 digits, 
        calculate the profit for each share, 
        set all combinations of shares. 
        params: 
            list_to_formate (list): list of shares from file. 
            max_amount (int): the amount constraint of buying shares. 
    """ 

    # registered_shares = formate_the_infos(sorted_list) 
    # calculated_shares = calculate_the_return(registered_shares) 

    basket = [] 
    total_purchase = float(0) 
    higher_purchase = float(0) 
    # profit = float(0) 
    total_benefit = round(float(0), 2) 
    best_basket = ()

    for row in sorted_list: 
        if round(float(row[1]), 2) > higher_purchase: 
            higher_purchase = round(float(row[1]), 2) 
            # min_purchase = max_purchase - higher_purchase 

    for i in range(len(sorted_list)): 
        combos = combinations(sorted_list, i + 1) 

    # sort the combos from higher benefit to smaller benefit 
    sorted_combos = sorted(combos, key=lambda x: x[3], reverse=True) 
    print(sorted_combos) 

    for combo in sorted_combos: 
        print(f'combo : {combo}') 
        # total_purchase = 0  # *** 
        # total_benefit = 0 

        for share in combo: 
            # if total_purchase < min_purchase: 
            #     basket.append(row) 
            #     profit += float(row[3]) 

            total_purchase += float(share[1]) 
            print(f'total_purchase OP126 : {total_purchase}') 

            if (total_purchase <= max_purchase): 
                basket.append(share) 
                total_benefit += round(float(share[3]), 2) 

                with open('data/combos_opti.csv', 'a', encoding='utf-8') as csvfile: 
                    csv_writer = csv.writer(csvfile, delimiter=',') 
                    csv_writer.writerow('-') 
                    csv_writer.writerows(combo) 

            else: 
                total_purchase -= round(float(share[1]), 2) 
                print(f'total_purchase OP139 : {total_purchase}') 

            # if profit > total_benefit:
            #     total_benefit = round(profit, 2) 
            #     print(f'total_benefit : {total_benefit}') 
            #     best_basket = combo 
    best_basket = sorted_combos[0] 

    return (best_basket, round(total_benefit, 2)) 


# def define_basket(list_to_chose, max_purchase): 
#     basket = [] 
#     total_purchase = 0 
#     higher_purchase = 0 
#     min_purchase = 0 
#     total_benefit = float(0) 
#     profit = float(0) 

#     for row in list_to_chose: 
#         if int(row[1]) > higher_purchase: 
#             higher_purchase = int(row[1]) 
#             min_purchase = max_purchase - higher_purchase 

#     for row in list_to_chose: 
#         total_purchase += int(row[1]) 
#         print(total_purchase) 
#         if total_purchase < min_purchase: 
#             basket.append(row) 
#             profit += int(row[3]) 
#         else: 
#             if total_purchase <= max_purchase: 
#                 basket.append(row) 
#                 profit += int(row[3]) 
#                 print(total_purchase) 
#             else: 
#                 total_purchase -= int(row[1]) 
#                 print(total_purchase) 
#                 break 
#         if profit > total_benefit: 
#             total_benefit = profit 

#     return (basket, total_purchase, total_benefit) 


if __name__ == '__main__': 
    print('name') 
    main() 

