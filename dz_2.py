i = 1
while i < 1001:
    a = i ** 3
    nechetak = a % 2
    if nechetak == 1:
        razbivka = sum([int(b) for b in str(a)])
        nechetak7 = razbivka // 7
    i += 2
    print(nechetak7)
    if nechetak7 == 0:
        plus_17 = razbivka + 17
        razbivka_17 = sum([int(c) for c in str(plus_17)])
        nechetak17 = razbivka_17 // 7
    i += 2
    print(nechetak17)
