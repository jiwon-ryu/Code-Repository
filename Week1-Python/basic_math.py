#######################
# Basic Math          #
#######################


def get_greatest(number_list):
    return max(number_list)


def get_smallest(number_list):
    return min(number_list)


def get_mean(number_list):
    return sum(number_list)/len(number_list)


def get_median(number_list):
    number_list.sort()
    return number_list[len(number_list)//2] if len(number_list)%2 == 1 else (number_list[len(number_list)//2-1] + number_list[len(number_list)//2])/2
