
# file deepcode ignore PythonDuplicateImport: Local project 
import csv 
from memory_profiler import profile 
import sys 
import time 


start_time = time.time() 


def main(): 

    FILENME = sys.argv[1] 
    MAX_AMOUNT = sys.argv[2] 

    registered_list = read_the_infos(FILENME) 

    benef_list = calculate_the_benefit(registered_list) 

    results = make_baskets(benef_list, MAX_AMOUNT) 

    display_results(results, FILENME, start_time, time) 


# @profile
def read_the_infos(FILENME): 
    """ Reads the infos file to get the actions, their prices 
            and their benefits. 
            Suppresses the first line from the result. 
        Returns:
            list: the formated actions from the file. 
    """ 
    registered_list = [] 
    with open(f'../enonce_et_ressources/{FILENME}.csv', 'r') as file: 
        fileReader = csv.reader(file, delimiter=',') 
        for row in fileReader: 
            registered_list.append(row) 
        registered_list.pop(0) 
    return registered_list 


# @profile
def calculate_the_benefit(registered_list): 
    """ Calculates the price * the benefit % for each action. 
        Args:
            registered_list (list): the list of shares to calculate. 
        Returns:
            list: the list with the calculated benefits. 
    """ 
    benef_list = [] 
    calculated_benefit = 0 

    for line in registered_list: 
        calculated_benefit = (float(line[1]) * float(line[2]) / 100)  # [:-1] 
        str(calculated_benefit).zfill(6) 
        line.append(round(float(calculated_benefit), 2)) 
        benef_list.append(line) 

    return benef_list 


# @profile
def column_to_sort(share): 
    return share[3] 


# @profile
def make_baskets(benef_list, MAX_AMOUNT):
    """ Read the file containing the share's list, 
        set all the pourcentages up to 2 digits, 
        calculate the profit for each share, 
        set all combinations of shares. 
        params: 
            list_to_formate (list): list of shares from file. 
            max_amount (int): the amount constraint of buying shares. 
    """ 
    purchase = round(float(0), 2) 
    basket = [] 
    benefit = round(float(0), 2) 

    sorted_list = sorted(benef_list, key=column_to_sort, reverse=True) 

    for s in sorted_list: 
        if (float(s[1]) <= float(0)) | (float(s[3]) < 1): 
            continue 
        elif float(s[1]) <= (float(MAX_AMOUNT) - float(purchase)): 
            purchase += round(float(s[1]), 2) 
            basket.append(s) 
            benefit += round(float(s[3]), 2) 

    results = { 
        'basket': basket, 
        'purchase': purchase, 
        'benefit': round(float(benefit), 2), 
        'ratio': (benefit / purchase) * 100, 
    } 

    return results 


# @profile
def display_results(results, FILENME, start_time, time): 
    # print(start_time) 
    # print(time.time()) 

    with open(f'data/{FILENME}-export.csv', 'a', encoding='utf-8') as csvfile: 
        # file deepcode ignore unquoted~csv~writer: local project 
        csv_writer = csv.writer(csvfile) 
        # adding header 
        file_name = [f'({sys.argv[1]}-export.csv)'] 
        headerList = ['name', 'price', 'profit'] 
        cost = [f'coût total : {round(results["purchase"], 2)}'] 
        profit = [f'profit total : {round(results["benefit"], 2)}'] 
        ratio = [f'ratio : {round(results["ratio"], 5)}'] 
        time_spent = [f'Time : {round(((time.time() - start_time)*1000), 5)} miliseconds'] 
        csv_writer.writerow(file_name) 
        csv_writer.writerow(headerList) 
        csv_writer.writerows(results['basket']) 
        csv_writer.writerow(cost) 
        csv_writer.writerow(profit) 
        csv_writer.writerow(ratio) 
        csv_writer.writerow(time_spent) 


if __name__ == '__main__': 

    main() 

