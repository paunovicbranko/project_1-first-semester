def Unos():
    lista1 = input().split(",")
    lista2 = input().split(",")
    return lista1, lista2
# Funkcija za unos listi

def Konverzija(lista1, lista2):
    lista1 = list(map(lambda x: int(x), lista1))
    lista2 = list(map(lambda x: int(x), lista2))
    return lista1, lista2
# Funkcija za konverziju clanova liste u Int

def Provera(lista1, lista2):
    try:
        Konverzija(lista1, lista2)
    except:
        return "Lista je prazna ili ste je pogrešno uneli!"
# Provera da li je moguće izvršiti funkciju Konverzija()

def anagram(lista1, lista2):
    for i in range(len(lista1)):

        if lista1.count(lista1[i]) == lista2.count(lista1[i]) and lista1.count(lista2[i]) == lista2.count(lista2[i]):
            a = True
        else:
            a = False
            break
    return a

def Ispis(lista1, lista2):
    if Provera(lista1, lista2) != "Lista je prazna ili ste je pogrešno uneli!":
        lista1, lista2 = Konverzija(lista1, lista2)
        print(anagram(lista1, lista2))

    else: print(Provera(lista1, lista2))

a,b = Unos()
Ispis(a, b)