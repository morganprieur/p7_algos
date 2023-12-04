







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

