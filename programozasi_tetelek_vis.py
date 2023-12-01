# Programozási tételek vizualizalasa
# By madorjan, 01/12/20023

def print_line_sep():
	print('='*40)


def list_visualizer(t, i):
	print(f'Index: {i}')
	print(f'Lista: {t}')
	pos = 8
	for k in range(0, i):
		pos += len(str(t[k])) + 2 + isinstance(t[k], str)*2
	print(pos*' ' + '↑')


def osszegzes(t):
	print()
	print('===Összegzés===')
	print()
	print('Bemeneti adatok:')
	print(f't lista: {t}')
	input()
	print_line_sep()
	osszeg = 0
	for i in range(len(t)):
		osszeg = osszeg + t[i]
		print(f'{i + 1}. iteráció')
		list_visualizer(t, i)
		print(f'Összeg: {osszeg}')
		print_line_sep()
		input()
	print(f'Az algoritmus végére értünk.')
	print(f'A listában szereplő elemek összege: {osszeg}')
	return osszeg


def megszamolas(t):
	print()
	print('===Megszámolás===')
	print()
	print('Bemeneti adatok:')
	print(f't lista: {t}')
	print(f'Feltétel: negatív szám')
	input()
	szamlalo = 0
	for i in range(len(t)):
		if t[i] < 0:
			szamlalo = szamlalo + 1
		print(f'{i + 1}. iteráció')
		list_visualizer(t, i)
		print(f'Feltétel: {t[i]} < 0 = {t[i] < 0}')
		print(f'Számláló: {szamlalo}')
		print_line_sep()
		input()
	print(f'Az algoritmus végére értünk.')
	print(f'A feltételnek {szamlalo} elem felelt meg.')
	return szamlalo


def eldontes_naiv(t, keresett_ertek):
	print()
	print('===Eldöntés - naiv megoldás===')
	print()
	print('Bemeneti adatok:')
	print(f't lista: {t}')
	print(f'Keresett érték: {keresett_ertek}')
	input()
	van = False
	for i in range(len(t)):
		if t[i] == keresett_ertek:
			van = True
		print(f'{i + 1}. iteráció')
		list_visualizer(t, i)
		print(f'Ez az elem a keresett érték? {t[i] == keresett_ertek}')
		print(f'Megtaláltuk már a listában a keresett értéket? {van}')
		print_line_sep()
		input()
	print(f'Az algoritmus végére értünk.')
	if van:
		print(f'A listában megtaláltuk a keresett értéket.')
	else:
		print(f'A listában nem találtuk meg a keresett értéket.')
	return van


def eldontes(t, keresett_ertek):
	print()
	print('===Eldöntés===')
	print()
	print('Bemeneti adatok:')
	print(f't lista: {t}')
	print(f'Keresett érték: {keresett_ertek}')
	input()
	i = 0
	print(f'{i + 1}. iteráció')
	list_visualizer(t, i)
	print(f'A lista végén állunk? {not(i < len(t))}')
	print(f'Megtaláltuk a keresett értéket? {not (t[i] != keresett_ertek)}')
	print(f'Kiléphetünk? {not (i < len(t) and t[i] != keresett_ertek)}')
	print_line_sep()
	input()
	while i < len(t) and t[i] != keresett_ertek:
		i = i + 1
		print(f'{i + 1}. iteráció')
		list_visualizer(t, i)
		print(f'A lista végén állunk? {not(i < len(t))}')
		if i < len(t):
			print(f'Megtaláltuk a keresett értéket? {not (t[i] != keresett_ertek)}')
			print(f'Kiléphetünk? {not (i < len(t) and t[i] != keresett_ertek)}')
		else:
			print(f'Megtaláltuk a keresett értéket? Az index túlmutat a lista utolsó elemén.')
			print(f'Kiléphetünk? True')
		print_line_sep()
		input()
	print(f'Az algoritmus végére értünk.')
	if i < len(t):
		print(f'A listában megtaláltuk a keresett értéket.')
		return True
	else:
		print(f'A listában nem találtuk meg a keresett értéket.')
		return False


def kivalasztas(t, keresett_ertek):
	print()
	print('===Kiválasztás===')
	print()
	print('Bemeneti adatok:')
	print(f't lista: {t}')
	print(f'Keresett érték: {keresett_ertek}')
	input()
	i = 0
	print(f'{i + 1}. iteráció')
	list_visualizer(t, i)
	print(f'Megtaláltuk a keresett értéket? {not (t[i] != keresett_ertek)}')
	print(f'Kiléphetünk? {not (i < len(t) and t[i] != keresett_ertek)}')
	print_line_sep()
	input()
	while t[i] != keresett_ertek:
		i = i + 1
		print(f'{i + 1}. iteráció')
		list_visualizer(t, i)
		print(f'Megtaláltuk a keresett értéket? {not (t[i] != keresett_ertek)}')
		print(f'Kiléphetünk? {not (i < len(t) and t[i] != keresett_ertek)}')
		print_line_sep()
		input()
	print(f'Az algoritmus végére értünk.')
	print(f'A listában a keresett elem indexe: {i}.')
	return i


def kereses(t, keresett_ertek):
	print()
	print('===Keresés===')
	print()
	print('Bemeneti adatok:')
	print(f't lista: {t}')
	print(f'Keresett érték: {keresett_ertek}')
	input()
	i = 0
	print(f'{i + 1}. iteráció')
	list_visualizer(t, i)
	print(f'A lista végén állunk? {not (i < len(t))}')
	print(f'Megtaláltuk a keresett értéket? {not (t[i] != keresett_ertek)}')
	print(f'Kiléphetünk? {not (i < len(t) and t[i] != keresett_ertek)}')
	print_line_sep()
	input()
	while i < len(t) and t[i] != keresett_ertek:
		i = i + 1
		print(f'{i + 1}. iteráció')
		list_visualizer(t, i)
		print(f'A lista végén állunk? {not (i < len(t))}')
		if i < len(t):
			print(f'Megtaláltuk a keresett értéket? {not (t[i] != keresett_ertek)}')
			print(f'Kiléphetünk? {not (i < len(t) and t[i] != keresett_ertek)}')
		else:
			print(f'Megtaláltuk a keresett értéket? Az index túlmutat a lista utolsó elemén.')
			print(f'Kiléphetünk? True')
		print_line_sep()
		input()
	if i < len(t):
		print(f'A listában megtaláltuk a keresett értéket, az indexe: {i}.')
		return True, i
	else:
		print(f'A listában nem találtuk meg a keresett értéket.')
		return False, -1


def masolas(t):
	print()
	print('===Másolás===')
	print()
	print('Bemeneti adatok:')
	print(f't lista: {t}')
	print(f'Művelet: négyzetre emelés')
	input()
	ki = []
	for i in range(len(t)):
		ki.append(t[i] ** 2)
		print(f'{i + 1}. iteráció')
		list_visualizer(t, i)
		print(f'Művelet: {t[i]} ** 2 = {t[i] ** 2}')
		print(f'Kimeneti lista: {ki}')
		print_line_sep()
		input()
	print(f'Az algoritmus végére értünk.')
	print(f'A kimeneti listánk: {ki}')
	return ki


def kivalogatas(t):
	print()
	print('===Kiválogatás===')
	print()
	print('Bemeneti adatok:')
	print(f't lista: {t}')
	print(f'Feltétel: negatív szám')
	input()
	ki = []
	for i in range(len(t)):
		if t[i] < 0:
			ki.append(t[i])
		print(f'{i + 1}. iteráció')
		list_visualizer(t, i)
		print(f'Feltétel: {t[i]} < 0 = {t[i] < 0}')
		print(f'Kimeneti lista: {ki}')
		print_line_sep()
		input()
	print(f'Az algoritmus végére értünk.')
	print(f'A kimeneti listánk: {ki}')
	return ki


def szetvalogatas(t):
	print()
	print('===Szétválogatás===')
	print()
	print('Bemeneti adatok:')
	print(f't lista: {t}')
	print(f'Feltétel: negatív szám')
	input()
	ki1 = []
	ki2 = []
	for i in range(len(t)):
		if t[i] < 0:
			ki1.append(t[i])
		else:
			ki2.append(t[i])
		print(f'{i + 1}. iteráció')
		list_visualizer(t, i)
		print(f'Feltétel: {t[i]} < 0 = {t[i] < 0}')
		print(f'Negatív számok listája: {ki1}')
		print(f'Nemnegatív számok listája: {ki2}')
		print_line_sep()
		input()
	print(f'Az algoritmus végére értünk.')
	print(f'Negatív számok listája: {ki1}')
	print(f'Nemnegatív számok listája: {ki2}')
	return ki1, ki2


def metszet(a, b):
	print()
	print('===Metszet===')
	print()
	print('Bemeneti adatok:')
	print(f'a lista: {a}')
	print(f'b lista: {b}')
	input()
	ki = []
	for i in range(len(a)):
		if a[i] in b:
			ki.append(a[i])
		print(f'{i + 1}. iteráció')
		list_visualizer(a, i)
		print(f'A(z) {a[i]} szerepel {b}-ben? {a[i] in b}')
		print(f'Metszet lista: {ki}')
		print_line_sep()
		input()
	print(f'Az algoritmus végére értünk.')
	print(f'A kimenet listája: {ki}')
	return ki


def unio(a, b):
	print()
	print('===Unió===')
	print()
	print('Bemeneti adatok:')
	print(f'a lista: {a}')
	print(f'b lista: {b}')
	input()
	ki = b
	print('Első lépésként a kimeneti listába belerakjuk a b lista értékeit')
	print(f'a lista: {a}')
	print(f'b lista: {b}')
	print(f'Kimeneti lista: {ki}')
	print_line_sep()
	input()
	for i in range(len(a)):
		old_ki = ki.copy()
		if a[i] not in ki:
			ki.append(a[i])
		print(f'{i + 1}. iteráció')
		list_visualizer(a, i)
		print(f'A(z) {a[i]} szerepel a {old_ki} kimeneti listában? {a[i] in old_ki}')
		print(f'Unió lista: {ki}')
		print_line_sep()
		input()
	print(f'Az algoritmus végére értünk.')
	print(f'A kimenet listája: {ki}')
	return ki


def maximum(t):
	print()
	print('===Maximum kiválasztás===')
	print()
	print('Bemeneti adatok:')
	print(f't lista: {t}')
	input()
	max_ertek = t[0]
	print(f'1. iteráció')
	list_visualizer(t, 0)
	print(f'Mivel még nincs maximum értékünk, legyen a jelenlegi elem a maximum.')
	print(f'Maximum: {max_ertek}')
	print_line_sep()
	input()
	for i in range(1, len(t)):
		old_max = max_ertek
		if max_ertek < t[i]:
			max_ertek = t[i]
		print(f'{i + 1}. iteráció')
		list_visualizer(t, i)
		print(f'Nagyobb a jelenlegi érték a maximumnál: {t[i]} > {old_max} = {t[i] > old_max}')
		print(f'Maximum: {max_ertek}')
		print_line_sep()
		input()
	print(f'Az algoritmus végére értünk.')
	print(f'A lista legnagyobb eleme: {max_ertek}')
	return max_ertek


def minimum(t):
	print()
	print('===Minimum kiválasztás===')
	print()
	print('Bemeneti adatok:')
	print(f't lista: {t}')
	input()
	min_ertek = t[0]
	print(f'1. iteráció')
	list_visualizer(t, 0)
	print(f'Mivel még nincs minimum értékünk, legyen a jelenlegi elem a minimum.')
	print(f'Minimum: {min_ertek}')
	print_line_sep()
	input()
	for i in range(1, len(t)):
		old_min = min_ertek
		if min_ertek > t[i]:
			min_ertek = t[i]
		print(f'{i + 1}. iteráció')
		list_visualizer(t, i)
		print(f'Kisebb a jelenlegi érték a minimumnál: {t[i]} < {old_min} = {t[i] < old_min}')
		print(f'Minimum: {min_ertek}')
		print_line_sep()
		input()
	print(f'Az algoritmus végére értünk.')
	print(f'A lista legkisebb eleme: {min_ertek}')
	return min_ertek


print()
print('Üdv!')
print('Ha még nem tetted, szedd ki a kommentet a program végén található valamely függvényhívás elől.')
print('Az algoritmusban az Enter billentyű segítségével léphetsz előre.')
print()
print_line_sep()
input()

# osszegzes([12, -2, 0, 3])

# megszamolas([-2, 132, 40, 0, -1, 50])

# eldontes_naiv(["alma", "korte", "banan", "ananasz", "megvalami"], "banan")

# eldontes_naiv(["alma", "korte", "banan", "ananasz", "megvalami"], "szilva")

# eldontes(["alma", "korte", "banan", "ananasz", "megvalami"], "ananasz")

# eldontes(["alma", "korte", "banan", "ananasz", "megvalami"], "szilva")

# ne felejtsük, kiválasztásnál a keresett érték BIZTOSAN szerepel a listában
# kivalasztas(["alma", "korte", "banan", "ananasz", "megvalami"], "ananasz")

# kereses(["alma", "korte", "banan", "ananasz", "megvalami"], "ananasz")

# kereses(["alma", "korte", "banan", "ananasz", "megvalami"], "szilva")

# masolas([3, 0, -2, 40])

# kivalogatas([-2, 132, 40, 0, -1, 50])

# szetvalogatas([-2, 132, 40, 0, -1, 50])

# metszet([1, 2, 3, 4, 5, 6], [2, 3, 5, 7, 11])

# unio([1, 2, 3, 4, 5, 6], [2, 3, 5, 7, 11])

# maximum([1, 8, 6, 12, 5])

# minimum([10, 3, 5, -3, 8])