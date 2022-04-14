info = 'инженер-конструктор Игорь', 'главный бухгалтер МАРИНА','токарь высшего разряда нИКОЛАй', 'директор аэлита'
for stroka in info:
    search = stroka.split()[-1].capitalize()
    print('Привет,', search,"!")