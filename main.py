#1
"""
1. Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot és ezeket tárolja el egy listában! A program számolja össze, és képernyőre írja ki a listában tárolt páros számok számát, valamint a lista elemeit!
"""
"""
import random
lista = []
paros = []
for i in range(5):
    lista.append(random.randint(1, 10))
print(f" a lista elemei: {lista}")
for i in lista:
    if i % 2 == 0:
        paros.append(i)
print(f"A lista páros számainak száma {len(paros)}")
"""

#-------------------------------

#2.1

"""
2.1 Feladat
A program számolja össze, hogy hány darab 'A' vagy 'a' betűvel kezdődő szó van az adott listában (amely a 'Próbáld ki!' gombra kattintva elérhető)! A képernyőre írja is ki a feltételnek megfelelő szavakat!
"""
"""
lista = []
szamlalo = 0
szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
for i in szavak:
    if i[0] == "A" or i[0] == "a":
        szamlalo += 1
        lista.append(i)
print(szamlalo)
print(lista)
"""

#---------------------------------------

#2.2
"""
2.2 Feladat
A program számolja össze, hogy hány darab 'E' vagy 'e' betűt tartalmazó szó van az adott listában (amely a 'Próbáld ki!' gombra kattintva elérhető)! A képernyőre írja is ki a feltételnek megfelelő szavakat!

"""
lista = []
szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']
for i in szavak:
    if 'e' in i or 'E' in i:
        lista.append(i)
        
   
print(f"Az e vagy E tartozo szavak száma: {len(lista)}")
print(f"A szavak amibkben van e vagy E: {lista}")


#-----------------------------------------------
