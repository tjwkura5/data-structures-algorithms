
def look_up(list):
    count = 0
    counts = {}
    for number  in list:
        counts[number] = counts.get(number, 0) + 1
        for two_power in range(4):
            second_num = (2 ** two_power) - number
            count += counts.get(second_num, 0)
    return count


print(look_up([-2, -1, 0, 1, 2]))
        
