import functools as ft

# lista = ['flower', 'flow', 'flight']
# print(ft.reduce(lambda x,y: x if len(x) > len(y) else y, lista))

# studenti = ['Vedad', 'Jasmin', 'Dejan', 'Dimitrije']
# ocjene = [6.0, 9.0, 8.5, 8.7]
# print(list(filter(lambda x: x[1] > 8.5, zip(studenti, ocjene))))

# lista_rjecnika = [{'ime': 'Ana', 'godine': 22, 'prosek': 9.1}, {'ime': 'Vedad', 'godine': 23, 'prosek': 7.3}, {'ime': 'Edin', 'godine': 20, 'prosjek': 6.0}]
# c = list(filter(lambda x: x['godine']>21, lista_rjecnika))
# c.sort(key=lambda x: x['prosek'])
# print(c)

# lista_rijeci = ["Hello, World!", "Python is cool", "Functional programming rocks"]
# print(ft.reduce(lambda x,y: x+y, list(map(lambda x: len(x.split(' ')), lista_rijeci))))

# srednja_ocjena = [('vedad',5,'biologija'), ('amar',3,'biologija'), ('vedad',5,'matematika'), ('amar',5,'matematika')]
# result = []
# [result.append(item) for item in list(map(lambda x: list(filter(lambda y: x[2]==y[2], srednja_ocjena)), srednja_ocjena)) if item not in result]
# print(result)
# print(list(map(lambda x: ft.reduce(lambda y,z: y[1]+z[1], x)/len(x), result)))

# voce = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# # Map each element to a dictionary with initial count of 1
# mapped = list(map(lambda x: {x: 1}, voce))
# # Merge dictionaries by adding counts for each element
# merged = ft.reduce(lambda x, y: {k: x.get(k, 0) + y.get(k, 0) for k in set(x) | set(y)}, mapped)
# print(merged)

# temperature = [11, 12, 34, 25, 11]
# t = temperature[0]
# print(list(map(lambda x: abs(x-temperature[temperature.index(x)+1]), temperature[:-1])))