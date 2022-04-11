n = int(input('Количество склонений: '))
for n in range(100):
    n = n +1
    i = {11, 12, 13, 14}
    if n in i:
        print(n, 'процентов')
    elif n % 10 == 1:
        print(n, 'процент')
    elif n % 10 > 1 and n % 10 < 5:
        print(n, 'процента')
    else:
        print(n, 'процентов')