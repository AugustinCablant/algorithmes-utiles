import random
"""
Complexité : La complexité moyenne du tri rapide pour n éléments est proportionnelle à n.log n, 
ce qui est optimal pour un tri par comparaison, mais la complexité dans le pire des cas est quadratique.

Concept : La méthode consiste à placer un élément du tableau (appelé pivot) à sa place définitive, en permutant 
tous les éléments de telle sorte que  tous ceux qui sont inférieurs au pivot soient à sa gauche et que tous ceux 
qui sont supérieurs au pivot soient à sa droite.
"""

#partitionnement
def partitionnement(L, debut, fin):
    """
    Étapes : 
    - le pivot est placé à la fin (arbitrairement), en l'échangeant avec le dernier élément du sous-tableau ;
    - tous les éléments inférieurs au pivot sont placés en début du sous-tableau ;
    - le pivot est déplacé à la fin des éléments déplacés.
    """
    pivot = L[fin]
    i = debut
    j = debut
    while j < fin:
        if L[j] <= pivot:
            L[i],L[j] = L[j],L[i]
            i += 1
        j += 1
    L[fin],L[i] = L[i],L[fin]
    return i

def tri_rapide(L, debut, fin):
    if debut < fin:
        i = partitionnement(L, debut, fin)
        tri_rapide(L,debut,i-1)
        tri_rapide(L,i+1,fin)


def tri_partition(liste):
    L = list(liste)
    tri_rapide(L, 0, len(L)-1)
    return L

liste = [2,4,8,10,1,2,3,12]
print(tri_partition(liste))
