def multiplicar(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiplicar(a,5)
print(b)
# salida:
# [2,4,10,16]

