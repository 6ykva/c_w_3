from utils import (json_load, list_sort, final_inf)


check_operations = json_load("../operations.json")
last_five_sorted = list_sort(check_operations)
final_information_list = final_inf(last_five_sorted)

for i in final_information_list:
    print(i)
