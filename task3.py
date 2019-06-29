from math import sqrt

lst_number = [2]


def simple_number(number_one, number_two, lst):
    for i in range(number_one, int(number_two) + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j > int((sqrt(i)) + 1):
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)


simple_number(3, 1000, lst_number)

for x in range(3, 1000):
    for j in range(len(lst_number)):
        flag = False
        if ((x - lst_number[j]) % 2 == 0):
            result = (x - lst_number[j]) / 2
            if (sqrt(result).is_integer()):
                flag = True
    if (not flag):
        print(x)
        break
