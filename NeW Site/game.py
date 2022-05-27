import random

print("Вибір: 0-Камінь,1-Ножниці,2-Бумага")
print("Камінь-Ножниці")
print("Ножниці-Бумага")
print("Бумага-Камінь")

r="Камінь"
s="Ножниці"
p="Бумага"

items =["r,s,p"]

print("Який ваш вибір?")
player= int(input("0-Камінь ,1-Ножниці ,2-Бумага"))

bot = random.randint(0,2)

if bot == 0 and player == 0:
    print("Вибір співпав")
elif bot == 1 and player == 2:
    print("Ви програли!")
if bot == 1 and player == 0:
    print("Ви виграли!")
elif bot == 2 and player == 0:
    print("Комп'ютер вас виграв :)")
if bot == 1 and player == 1:
    print("Нічия")
elif bot == 2 and player == 2:
    print("Нічия")
if bot == 2 and player == 1:
    print("Компютер виявився розумнішим і ви отримали поразку :( !")
elif bot == 0 and player == 1:
    print("Ви програли!")
if bot == 0 and player ==2:
    print("Комп'ютер отримав поразку!")

# import random

# print("Вітаю в грі Хто більше?")
# print("Правила гри вибрати число від 0-100 і то1 гравець у якого число більше за число противника - Виграє!")
# print("Вибір від 0 до 100")
# print("Який ваш вибір?")
# player= int(input("0-100"))

# bot = random.randint(0,100)
# if bot >= 50 and player <= 50:
#     print("Ви виграли!")
# if bot <= 50 and player >= 50:
#     print("Ви програли!")    