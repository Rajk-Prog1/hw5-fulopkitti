def dragon_solution(is_dead, number_of_cows):
    fat_alive_cow_index = 0
    thin_alive_cow_index = number_of_cows - 1
    also_hatar=0
    felso_hatar=0
    
    while (fat_alive_cow_index + 1) < thin_alive_cow_index:
        middle_cow = int((fat_alive_cow_index + 
                          thin_alive_cow_index) / 2)
        if is_dead(middle_cow):
            thin_alive_cow_index = middle_cow
        else:
            fat_alive_cow_index = middle_cow
    
    return middle_cow