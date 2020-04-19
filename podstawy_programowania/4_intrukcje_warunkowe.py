x = 6
if x==5:
    print('x jest równe 5')
    print('x jest równe:',x)
else:
    print('x nie jest równe 5')
    print('x wynosi:',x)


##################################

y = True

if y:
    print('prawda')
else:
    print('fałsz')

##################################

z = 5 > 6

if z:
    print('prawda')
else:
    print('fałsz') 

##################################

j = '1'
j = '0'

j = ''
j = False

if bool(j):
    print(1)
else:
    print(0)  

##################################

k = input('Podaj k: ')
if bool(k):
    print("Zmienna k zawiera dane")
else:
    print("Zmienna k nie zawiera danych")
