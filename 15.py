'''
Обозначим через ДЕЛ(n,m) утверждение «натуральное число n делится без остатка на натуральное число m».
Пусть на числовой прямой дан отрезок B=[132;150]. Для какого наименьшего натурального числа А большего 1 логическое выражение
(¬ДЕЛ(x,A)∧(x∈B))→¬ДЕЛ(x,13)
истинно (т. е. принимает значение 1) при любом целом положительном значении переменной х?
'''
for a in range(2,500):
    s=1
    for x in range(2,500):
        if not((x%a!=0 and 132<=x<=150) <= (x%13!=0)):
            s = 0
    if s == 1:
        print(a)

