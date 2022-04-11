duration = int(input("duration = "))
day = (duration // (24 * 60 ** 2))
hour = (duration // (60 ** 2) - 24 * day)
minutes = (duration // 60 % 60)
seconds = duration % 60
if duration > 0 and duration < 60:
    print(seconds, 'cек')
if duration > 60 and duration < 3600:
    print(minutes, 'мин', seconds, 'cек')
if duration > 3600 and duration < 86400:
    print(hour, 'час', minutes, 'мин', seconds, 'cек')
if duration > 86400:
    print(day, 'дн', hour, 'час', minutes, 'мин', seconds, 'cек')
if duration < 0:
    print('Не в то время живешь) ')