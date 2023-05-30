for x in range(0, 151):
    print(x)

for x in range(5,1001,5):
    print(x)



for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0
for x in range(1, 500001, 2):
    sum += x

print(f"La suma final es: {sum}")



inicio = 2018

while inicio > 0:
    print(inicio)
    inicio -= 4

lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)

