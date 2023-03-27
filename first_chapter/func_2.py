def summator(a,b,c,d,*args,**kwargs):
    if kwargs:
        return sum(kwargs.values()) + sum((a,b,c,d)) + sum(args)
    return sum((a,b,c,d)) + sum(args)

"""
1)Если вызвать функцию с 1 аргуметом упадёт ошибка TypeError. Не хватка аргументов.
2)a,b,c,d = 1,2,3,4
print(summator(a=a,b=b,c=c,d=d))
3)tup = (1,2,3,4,9)
print(summator(*tup))
4) Я немного запутался и переписал фукцию чтобы считала со словарем. Но если мы передаем с одной * ,то будет список ключей
,а если с 2 то мы можем обращаться со словарём
brawl_stars = dict(Brok=709,Baron=640,Spike=730,Crow=500)
print(summator(1,2,3,4,**brawl_stars))
"""
