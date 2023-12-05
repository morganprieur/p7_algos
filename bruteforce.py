
import csv 
from itertools import combinations 
from tqdm import tqdm 


def main(): 
    # print('main') 

    registered_shares = read_the_infos() 
    formated_shares = formate_the_infos(registered_shares) 
    calculated_shares = calculate_the_return(formated_shares) 
    basket_bruteforce = make_combos(calculated_shares, 500) 
    print(basket_bruteforce) 


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
    formated_shares = [] 
    for new_row in list_to_formate: 
        new_benef = new_row.pop(2) 
        new_row.append(new_benef.zfill(3)) 
        formated_shares.append(new_row) 
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
        calculated_benefit = (float(line[1]) * float(line[2][:2])) / 100 
        line.append(calculated_benefit) 
        calculated_list.append(line) 

    return calculated_list 


def make_combos(calculated_shares, max_purchase):
    """ Read the file containing the share's list, 
        set all the pourcentages up to 2 digits, 
        calculate the benefit for each share, 
        set all combinations of shares. 
        params: 
            list_to_formate (list): list of shares from file. 
            max_purchase (int): the amount constraint of buying shares. 
    """ 
    benefit = 0 
    best_basket = [] 

    for i in range(len(calculated_shares)): 
        combos = combinations(calculated_shares, i + 1) 

        for combo in combos: 
            print(f'combo : {combo}') 
            total_purchase = 0 
            combo_benefit = 0 

            for share in combo: 
                total_purchase += float(share[1]) 
                # print(f'total_purchase : {total_purchase}') 
                if total_purchase <= max_purchase: 
                    combo_benefit += share[3] 

                    with open('data/combos_bf.csv', 'a', encoding='utf-8') as csvfile: 
                        csv_writer = csv.writer(csvfile, delimiter=',') 
                        csv_writer.writerow('- ') 
                        csv_writer.writerows(combo) 

                else: 
                    total_purchase -= float(share[1]) 
                    # print(f'total_purchase BF86 : {total_purchase}') 

                if combo_benefit > benefit:
                    benefit = combo_benefit 
                    # print(f'benefit : {benefit}') 
                    best_basket = combo 

    return best_basket 



if __name__ == '__main__': 
    # print('name') 
    main() 

