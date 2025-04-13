# Programozási tételek
# By madorjan, 01/12/2023
# Pszeudokód forrása: https://szit.hu/doku.php?id=oktatas:programozas:programozasi_tetelek:mondatszeru_leiras

# Összegzés
# Adott egy t, számokat tartalmazó lista, kimenetként várjuk a listában szereplő számok összegét
# elemek összegét
# python shorthand: sum(t)

# osszeg = 0
# ciklus i = 0 .. n -1
#     osszeg = osszeg + t[i]
# ciklus vége
# ki osszeg

def osszegzes(t):
	osszeg = 0
	for i in range(len(t)):
		osszeg = osszeg + t[i]
	return osszeg

# Megszámolás
# Adott egy t lista és egy f feltétel, kimenetként várjuk, a listánkban hány elem felet meg f feltételnek
# python shorthand: len(t)
#
# Pl.: hány negatív szám van a listában
# szamlalo = 0
# ciklus i = 0 .. n - 1
#     ha t[i] < 0 akkor
#         szamlalo = szamlalo + 1
#     ha vége
# ciklus vége
# ki szamlalo

def megszamolas(t, feltetel):
	szamlalo = 0
	for i in range(len(t)):
		if feltetel(t[i]):
			szamlalo = szamlalo + 1
	return szamlalo


# Eldöntés
# Adott egy t lista és egy keresett_ertek változó, kimenetként várunk egy boolean értéket,
# hogy a listában szerepel-e a keresett ertek.
# python shorthand: keresett_ertek in t
#
# Naiv algoritmus - minden esetben végignézi a lista összes elemét, akkor is, ha már megtaláltuk a keresett értéket:
# van = 0
# ciklus i = 0 .. n-1
# 	ha tomb[i] = keresett_ertek akkor
# 		van = 1
# 	ha vége
# ciklus vége
# ki van

def eldontes_naiv(t, keresett_ertek):
	van = False
	for i in range(len(t)):
		if t[i] == keresett_ertek:
			van = True
	return van

# Optimalizált algoritmus - azonnal megáll, ha megtaláltuk a keresett értéket:
# i = 0
# ciklus amíg i<n és t[i]<> ker
#     i=i+1
# ciklus vége
# Ha i<n akkor
#     ki "Van ilyen"
# különben
#     ki "A keresett érték nem található"
# ha vége

def eldontes(t, keresett_ertek):
	i = 0
	while i < len(t) and t[i] != keresett_ertek:
		i = i + 1
	if i < len(t):
		return True
	else:
		return False

# Kiválasztás
# Adott egy t lista, valamint egy, a listában biztosan szereplő keresett_ertek, kimenetként szeretnénk tudni a
# keresett_ertek indexét a listában.
# python shorthand: t.index(keresett_ertek)
#
# i = 0
# ciklus amíg tomb[i] <> ker
#     i = i + 1
# ciklus vége
# ki i

def kivalasztas(t, keresett_ertek):
	i = 0
	while t[i] != keresett_ertek:
		i = i + 1
	return i

# Keresés
# Adott egy t lista, valamint egy keresett_ertek változó. Kimenetként várunk egy boolean értéket, hogy a változó
# szerepel-e az adott helyen, és ha igen, mi az indexe.
# python shorthand: t.find(keresett_ertek)
#
# ker = 30
# i = 0
# ciklus amíg i<n és t[i]<>ker
#     i = i + 1
# ciklus vége
#
# Ha i<n akkor
#     ki "Van ilyen"
#     ki: "Indexe: ", i
# különben
#     ki: "A keresett érték nem található"
# ha vége

def kereses(t, keresett_ertek):
	i = 0
	while i < len(t) and t[i] != keresett_ertek:
		i = i + 1
	if i < len(t):
		return True, i
	else:
		return False, -1

# Másolás
# Adott egy t lista, valamint egy művelet. Kimenetként várunk egy listát, amin a t elemein végrehajtunk egy műveletet.
# python shorthand: ki = [muvelet(x) for x in t]
#
# ciklus i = 1 .. n
#     b[i] = művelet(a[i]) //valamilyen művelet a[i]-vel
# ciklus vége

def masolas(t, muvelet):
	ki = []
	for i in range(len(t)):
		ki.append(muvelet(t[i]))
	return ki

# Kiválogatás
# Adott egy t lista, valamint egy f feltétel. Kimenetként várunk egy listát, ami t azon elemeit tartalmazza, ami megfelel
# az f feltételünknek.
# python shorthand: filter(f, t)
# python shorthand listaművelettel: ki = [x for x in t if f(x)]
#
# Pl. x < 5 feltetel mellett
# j = 0
# ciklus i = 0 .. n - 1
#     ha a[i] < 5
#         b[j] = a[i]
#         j = j + 1
#     ha vége
# ciklus vége

def kivalogatas(t, feltetel):
	ki = []
	for i in range(len(t)):
		if feltetel(t[i]):
			ki.append(t[i])
	return ki

# Szétválogatás
# Adott egy t lista, valamint egy f feltétel. Kimenetként várunk két listát, az egyikben t f feltételnek megfelelő elemeit,
# a másikban a feltételnek nem megfelelő elemeit várjuk.
# python shorthand: nincs, de nagyon könnyen készíthetünk magunknak egyet a kiválogatásban látottakkal, pl.
# 	ki1 = [x for x in t if f(x)]
# 	ki2 = [x for x in t if not(f(x))]
#
# j = 0
# k = 0
# ciklus i = 0 .. n-1
#     ha a[i] < 5
#         b[j] = a[i]
#         j = j + 1
#     különben
#         c[k] = a[i]
#         k = k + 1
#     ha vége
# ciklus vége

def szetvalogatas(t, feltetel):
	ki1 = []
	ki2 = []
	for i in range(len(t)):
		if feltetel(t[i]):
			ki1.append(t[i])
		else:
			ki2.append(t[i])
	return ki1, ki2

# Metszet
# Adott a és b lista. Kimenetként várunk egy listát a és b közös elemeivel.
# python shorthand: kozos = [x for x in a if x in b]
#
# k = 0
# ciklus i = 0 .. n-1
#     j = 0
#     ciklus amíg j<m és b[j]<>a[i]
#         j = j + 1
#     ciklus vége
#     ha j<m akkor
#         c[k] = a[i]
#         k = k + 1
#     ha vége
# ciklus vége

def metszet(a, b):
	ki = []
	for i in range(len(a)):
		if a[i] in b:
			ki.append(a[i])
	return ki

# Unió
# Adott a és b lista. Kimenetként várunk egy listát, amelyben a és b minden eleme szerepel pontosan egyszer.
# python shorthand: unio = list(set(a) | set(b))
#
# ciklus i = 0 .. n-1
#     c[i] = a[i]
# ciklus vége
# k = n
# ciklus j = 0 .. m-1
#     i = 0
#     ciklus amíg i<n és b[j]<>a[i]
#         i = i + 1
#     ciklus vége
#     ha i>=n akkor
#         c[k] = b[j]
#         k = k + 1
#     ha vége
# ciklus vége

def unio(a, b):
	ki = a
	for i in range(len(b)):
		if b[i] not in ki:
			ki.append(b[i])
	return ki

# Maximum kiválasztás
# Adott t, rendezhető elemekből álló lista. Kimenetként várjuk a lista legnagyobb értékű elemét.
# python shorthand: max(t)
#
# max = t[0]
# ciklus i = 1 .. n - 1
#     ha t[i]> max akkor
#         max = t[i]
#     ha vége
# ciklus vége
# ki max

def maximum(t):
	max_ertek = t[0]
	for i in range(1, len(t)):
		if max_ertek < t[i]:
			max_ertek = t[i]
	return max_ertek

# Minimum kiválasztás
# Adott t, rendezhető elemekből álló lista. Kimenetként várjuk a lista legkisebb értékű elemét.
# python shorthand: min(t)
#
# min=t[0]
# ciklus i = 1 .. n-1
#     ha t[i] < min
#         min = t[i]
#     ha vége
# ciklus vége
# ki min

def minimum(t):
	min_ertek = t[0]
	for i in range(1, len(t)):
		if min_ertek > t[i]:
			min_ertek = t[i]
	return min_ertek