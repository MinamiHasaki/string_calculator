import re


def add(number_string):
    if not number_string:
        return 0
    if number_string:
        delimiter = '[' + number_string.split('\n')[0] + '\n' + ',' + ']+'
        number_list = re.split(delimiter, number_string.split('\n', 1)[1])
        number_sum = 0
        negatives = []
        for i in range(len(number_list)):
            if int(number_list[i]) < 0:
                negatives.append(number_list[i])
            if 0 < int(number_list[i]) < 1000:
                number_sum = number_sum + int(number_list[i])
        if negatives:
            return f"negatives not allowed:{negatives}"
        else:
            return number_sum


print(add("//;\n1;2,3,4,5,6,7,8,9"))
