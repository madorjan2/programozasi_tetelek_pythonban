# Programozási tételek vizualizálása

Ez a Python szkript a programozási tételeket vizualizálja lépésről lépésre, hogy segítse a megértésüket. A szkript a következő tételeket mutatja be:

* Összegzés
* Megszámolás
* Eldöntés (naiv és optimalizált változat)
* Kiválasztás
* Keresés
* Másolás
* Kiválogatás
* Szétválogatás
* Metszet
* Unió
* Maximum kiválasztás
* Minimum kiválasztás

## Használat

1.  A különböző algoritmusok bemutatásához távolítsa el a kommentet a szkript végén található valamelyik függvényhívás elől, majd futtassa újra a szkriptet. Például az összegzés tételének megtekintéséhez módosítsa a következőt:
    ```python
    # osszegzes([12, -2, 0, 3])
    ```
    erre:
    ```python
    osszegzes([12, -2, 0, 3])
    ```
    A paraméterben megadott listák szabadon változtathatóak.
2.  Futtassa a szkriptet a következő paranccsal:
    ```bash
    python programozasi_tetelek_vis.py
    ```
3.  A program elindul, és üdvözlő üzenetet jelenít meg. Kövesse a képernyőn megjelenő utasításokat. 
4.  Az algoritmusok lépésenként haladnak előre. Az Enter billentyű megnyomásával léphet a következő iterációra. A program minden lépésnél megjeleníti a lista aktuális állapotát, a vizsgált indexet, a feltételek kiértékelését (ha van), és a részeredményeket.

## Függvények

A szkript a következő függvényeket tartalmazza, melyek az egyes programozási tételeket implementálják:

* `osszegzes(t)`: Egy lista elemeinek összegét számítja ki.
* `megszamolas(t)`: Megszámolja, hogy egy adott feltételnek hány elem felel meg a listában.
* `eldontes_naiv(t, keresett_ertek)`: Eldönti, hogy egy adott érték szerepel-e a listában (naiv megközelítés).
* `eldontes(t, keresett_ertek)`: Eldönti, hogy egy adott érték szerepel-e a listában (optimalizált megközelítés).
* `kivalasztas(t, keresett_ertek)`: Megkeresi egy adott érték indexét a listában (feltételezve, hogy az érték biztosan szerepel).
* `kereses(t, keresett_ertek)`: Megkeresi egy adott érték indexét a listában, és jelzi, ha nem található meg.
* `masolas(t)`: Létrehoz egy új listát, amely az eredeti lista elemeinek valamilyen transzformációját tartalmazza (jelen esetben négyzetre emelés).
* `kivalogatas(t)`: Létrehoz egy új listát, amely az eredeti lista azon elemeit tartalmazza, amelyek megfelelnek egy adott feltételnek.
* `szetvalogatas(t)`: Két új listát hoz létre, az egyik a megadott feltételnek megfelelő, a másik a nem megfelelő elemekkel.
* `metszet(a, b)`: Meghatározza két lista metszetét (azokat az elemeket, amelyek mindkét listában szerepelnek).
* `unio(a, b)`: Meghatározza két lista unióját (azokat az elemeket, amelyek legalább az egyik listában szerepelnek).
* `maximum(t)`: Megkeresi a lista legnagyobb elemét.
* `minimum(t)`: Megkeresi a lista legkisebb elemét.

## Megjegyzések

* A szkript interaktív módon működik, így minden lépést a felhasználó hagy jóvá az Enter megnyomásával.
* A szkript végén található kommentált függvényhívások segítségével lehet kipróbálni az egyes tételeket különböző bemeneti adatokkal.

## Szerző

madorjan - 2023. december 1.
