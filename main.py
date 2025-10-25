import math
import random
print("1  задание:")
entersize=input("Введите размер треугольника(число): ")
try:
    size=int(entersize)

    dist1=size-1
    dist2=0
    dist3=1
    for i in range(size-1):
        if dist2==0:
            print("  "*dist1+"* "*dist3+"  "*dist1)
            dist2+=1
            dist3+=1
            dist1-=1
        else:
            print("  "*dist1+"*  "+"  "*dist2+"*   "+" "*dist1)
            dist2+=2
            dist1-=1
    print("*  "*(size+math.floor(size/2.5)))
except:
    print("А вот не надо было вводить строку там, где просят ввести число.")
print("2 задание:")
inter=input("Введите промежуток(пример: 2, 5): ")
num=input("Введите число: ")
try:
    realnum = int(num)
    minn, maxx = inter.split(", ")
    if int(minn) >= int(maxx):
        print("Минимальное число не может быть равно или больше чем максимальное число.")
    if realnum >= int(minn) and realnum <= int(maxx):
        print("Число входит в промежуток.")
    else:
        print("Число не входит в промежуток.")
except:
    print("Ошибка. Убедитесь, что вы корректно ввели промежуток и ввели в следующий ввод число.")

siz=input("Введите кол-во чисел в матрице(ЧИСЛО!!!!): ")
try:
    global n
    n=int(siz)
except:
    print("Надо было число вводить")
matrix = [[random.randint(0,9)for i in range(n)] for v in range(n)]

for row in matrix:
    for i in range(len(row)):
        if i == 0:
            row[size-1] = row[i]
        elif i < (size-1):
            row[i-1] = row[i]
    for element in row:
        print(element, end="  ")
    print()
