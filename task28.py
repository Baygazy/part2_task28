all_numbers = input("Введите положительные и отрицательные числа: ").split() # Стандартно элементы в списке будут str
int_all_numbers = []
re_all_numbers = []
for x in all_numbers:
    int_all_numbers.append(int(x))     # преобразуем в инт номера в списке для удобства последующей операции сними

for i in int_all_numbers:
    if i < 0:
        re_all_numbers.append(-1)
    elif i > 0:
        re_all_numbers.append(1)
    elif i == 0:
        re_all_numbers.append(i)
    else:
        None
print("Положительные числа: ", re_all_numbers)
