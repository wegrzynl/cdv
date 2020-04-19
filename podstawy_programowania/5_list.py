programowanie = ['Python', 'PHP', 'C#', 'JS', 'Java']
print(programowanie)
print(type(programowanie))

first = programowanie[0]
print(first)

threeElement = programowanie[0:3]
print(threeElement)

lastElement = programowanie[-1]
print(lastElement)

#Dodawanie nowego elementu na koniec listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

#zliczanie elementów w liście
countElements = programowanie.count('Python')
print(countElements)

#ilość elementów w liście
countElementsOfList = len(programowanie)
print(countElementsOfList)

#połączenie list
anotherList = ['C', 'C++']
programowanie.extend(anotherList)
print(programowanie)
print(anotherList)

#czyszczenie list
new = programowanie
print('Lista nowa: ', end="")
print(new)
new.clear()
print('Lista nowa: ', end="")
print(new)

print('Lista programowanie: ', end="")
print(programowanie)