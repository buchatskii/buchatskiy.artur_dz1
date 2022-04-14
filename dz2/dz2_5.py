list = [57.8, 46.51, 98.04, 47.94, 24.01, 12.39, 04.05, 23, 94.05, 49.04]
list_sort = sorted(list)
for add in list_sort:
        print(str(int(add)).zfill(2) + ' руб. ' + str((int(add * 100) % 100)).zfill(2) + ' коп.')
    #добавить два нуля и убрать их
