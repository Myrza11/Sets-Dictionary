'''#первое задание
a = {3,10,11,13,31,21,1,10,3,5,6,6}
a.remove(6)
print(a)


#втарое задание
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1.intersection_update(farm_2)
print(farm_1)

#третье задание
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
z = farm_2.difference(farm_1)
print(z)

#четвёртое задание
a = {12,23,43,45,56}
b = {26,90}
a.update(b)
print(a)

#пятое задание 
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu["besh_barmak"] = 130
print(menu)
menu["besh_barmak"] = 135
print(menu)


#шестое задание
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
drink =['Coca-Cola', 'Sprite', 'Fanta']
menu["drinks"] = ['Coca-Cola', 'Sprite', 'Fanta']
print(menu)

#cедьмое задание
set1={"add","remove","clear","update","difference","discard","intersection","pop"}
set2={"clear","keys","items","get","values","update"}
set2.intersection_update(set1)
print(set2)

#восьмое задание
s = {}
i=0
while i < 3: 
	a = input("введите ваше имя")
	d = input("введите ваш пароль")
	i+=1
	s[a] = d
	print(s)

#девятое задание
a = set()
i=0
while i < 10:
	i+=1
	s = input("введите число")
	a.add(s)
print(a)



#десятое задание
a = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
b = a.remove('Suriname')
print(b)
print(a)


#одиннадцатое задание
suitcase = []
a = suitcase.append("щётка")
a = suitcase.append("карандаш")
a = suitcase.append("паста")
a = suitcase.append("йогурт")
a = suitcase.append("ремень")
print(a)
print(suitcase)
suitcase.pop()
print(a)
print(suitcase)


#двеннадцатое задание
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1.intersection_update(farm_2)
print(farm_1)

'''

#тринадцатое задание
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
s = farm_1.difference(farm_2)
print(s)






