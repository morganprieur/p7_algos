
import csv 
from itertools import combinations 


def main(): 
    print('main') 

    registered_actions = read_the_infos() 
    test_bf = make_combos(registered_actions, 500) 
    print(test_bf) 


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


def make_combos(list_to_formate, max_amount):
    """ Read the file containing the share's list, 
        set all the pourcentages up to 2 digits, 
        calculate the profit for each share, 
        set all combinations of shares. 
        params: 
            list_to_formate (list): list of shares from file. 
            max_amount (int): the amount constraint of buying shares. 
    """ 

    registered_shares = formate_the_infos(list_to_formate) 
    calculated_shares = calculate_the_return(registered_shares) 

    profit = 0 
    best_combo = [] 

    for i in range(len(calculated_shares)): 
        combos = combinations(calculated_shares, i + 1) 

        for combo in combos: 
            print(f'combo : {combo}') 
            total_amount = 0 
            total_benefit = 0 

            for share in combo: 
                total_amount += float(share[1]) 
                print(f'total_amount : {total_amount}') 
                if total_amount <= max_amount: 
                    total_benefit += share[3] 

                    with open('data/combos.csv', 'a', encoding='utf-8') as csvfile: 
                        csv_writer = csv.writer(csvfile, delimiter=',') 
                        csv_writer.writerow('-') 
                        csv_writer.writerows(combo) 

                else: 
                    total_amount -= float(share[1]) 
                    print(f'total_amount BF86 : {total_amount}') 

                if total_benefit > profit:
                    profit = total_benefit 
                    print(f'profit : {profit}') 
                    best_combo = combo 

    return best_combo 


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


if __name__ == '__main__': 
    print('name') 
    main() 

