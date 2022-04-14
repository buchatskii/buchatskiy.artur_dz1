arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
sign = 0
while i < len(arr):
    if arr[i][0] in '+-':
        sign = arr[i][0]
    if arr[i].isdigit() or (sign and arr[i][1:].isdigit()):
        if sign:
            arr[i] = sign + arr[i][1:].zfill(2)
        else:
            arr[i] = arr[i].zfill(2)

        arr.insert(i, '"')
        arr.insert(i + 2, '"')
        i += 2
    i += 1

str1 = ''
for ar2 in arr:
    if '"' in ar2:
        continue
    str1 = str1 + " " + ar2
print(str1)