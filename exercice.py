#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        return(-number)
    else:
        return(number)


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    list = []
    for prefixe in prefixes:
        list.append(prefixe+suffixe)
    return list


def prime_integer_summation() -> int:
    liste_premiers = []
    nombre_teste = 2
    while len(liste_premiers) < 100:
        prime = True
        root = math.sqrt(nombre_teste)
        for premier in liste_premiers:
            if nombre_teste%premier == 0:
                prime = False
                break
            if premier >= root:
                break
        if prime:
            liste_premiers.append(nombre_teste)
        nombre_teste += 1
    return sum(liste_premiers)



def factorial(number: int) -> int:
    factorielle = number
    for produit in range(1,number):
        factorielle *= produit
    return(factorielle)


def use_continue() -> None:
    for a in range(1,11):
        if a == 5:
            continue
        else:
            print(a)

def verify_age_one_group(group):
    if len(group) < 3 or len(group) > 10:
        return False
    elif 25 in group:
        return True
    else:
        for individu in group:
            if individu < 18:
                return False
            if individu > 70 and 50 in group:
                return False
    return (True)

def verify_ages(groups: List[List[int]]) -> List[bool]:
    liste_accepte = []
    for group in groups:
        liste_accepte.append(verify_age_one_group(group))
    return(liste_accepte)



def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
