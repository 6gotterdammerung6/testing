intConvert = 2149583361

IP_array = [''] * 32
IP_array[0] = 1
array = 1

#Sets values to subtract for identifying binary
for i in IP_array:
    if i == 0:
        continue
    elif i >= 2147483648:
        break
    else:
        IP_array[array] = IP_array[array-1] * 2
        print(IP_array)
        array = array + 1
