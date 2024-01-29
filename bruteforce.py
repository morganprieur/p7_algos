
import csv 
from itertools import combinations 
from memory_profiler import profile 
import sys 
import time 


start_time = time.time() 


def main(): 

    FILENAME = sys.argv[1] 
    MAX_AMOUNT = sys.argv[2] 

    registered_list = read_the_infos(FILENAME) 

    calculated_list = calculate_the_return(registered_list) 

    results = make_combos(calculated_list, MAX_AMOUNT, start_time, time, FILENAME) 

    display_results(results, FILENAME, time) 


# @profile
def read_the_infos(FILENAME): 
    """ Reads the infos file to get the actions, their prices 
            and their benefits. 
            Suppresses the first line from the result. 
        Returns:
            list: the formated actions from the file. 
    """ 
    registered_actions = [] 
    with open(f'data/{FILENAME}.csv', 'r') as csv_file: 
        fileReader = csv.reader(csv_file, delimiter=',') 
        for row in fileReader: 
            registered_actions.append(row) 
        registered_actions.pop(0) 

    return registered_actions 


# @profile
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
        calculated_benefit = (float(line[1]) * float(line[2])) / 100 
        line.append(calculated_benefit) 
        calculated_list.append(line) 

    return calculated_list 


# @profile
def make_combos(list_to_combine, MAX_AMOUNT, start_time, time, FILENAME):
    """ Modifies all the pourcentages up to 2 digits, filling them with zeros, 
        calculates the benefit for each share, 
        makes all combinations of shares. 
        params: 
            list_to_combine (list): list of shares from file. 
    """ 
    benefit = 0 
    best_basket = [] 

    for i in range(len(list_to_combine)): 
        combos = combinations(list_to_combine, i + 1) 

        for combo in combos: 
            total_purchase = 0 
            combo_benefit = 0 

            for share in combo: 
                total_purchase += float(share[1]) 
                if float(total_purchase) <= float(MAX_AMOUNT): 
                    combo_benefit += share[3] 
                else: 
                    total_purchase -= float(share[1]) 

                if combo_benefit > benefit:
                    benefit = combo_benefit 
                    best_basket = combo 

    time_spent = f'{round((time.time() - start_time)*1000)} miliseconds' 

    results = { 
        'best_basket': best_basket, 
        'benefit': benefit, 
        'total_purchase': total_purchase, 
        'ratio': float(benefit) / float(total_purchase) * 100, 
        'time_spent': time_spent, 
    } 

    return results  


# @profile
def display_results(results, FILENAME, time): 

    print('Meilleure combi force brute (fichier de 20 actions) : ') 
    for share in results['best_basket']: 
        print('\t', share) 

    print(f''' 
        Bénéfice : {round(results['benefit'], 2)} \n 
        Coût total : {round(results['total_purchase'], 2)} \n 
        Coût ratio : {round(results['ratio'], 5)} \n 
        Temps : {str(results['time_spent'])} 
    ''') 

    with open(f'data/{FILENAME}-bf.csv', 'a', encoding='utf-8') as csvfile: 
        csv_writer = csv.writer(csvfile, delimiter=',') 
        file_name = [f'({sys.argv[1]}-export.csv)'] 
        headerList = ['name', 'price', 'profit'] 
        time_spent = [f'Time : {round(((time.time() - start_time)*1000), 5)} miliseconds'] 

        cost = [f'coût total : {round(results["total_purchase"], 2)}'] 
        profit = [f'profit total : {round(results["benefit"], 2)}'] 
        ratio = [f'ratio : {round(results["ratio"], 5)}'] 
        time = [f'Time : {round(((time.time() - start_time)*1000), 5)} miliseconds'] 
        csv_writer.writerow(file_name) 
        csv_writer.writerow(headerList) 
        csv_writer.writerows(results['best_basket']) 
        csv_writer.writerow(cost) 
        csv_writer.writerow(profit) 
        csv_writer.writerow(ratio) 
        csv_writer.writerow(time_spent) 


if __name__ == '__main__': 

    main() 

