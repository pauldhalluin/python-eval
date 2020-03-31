# -*- coding: utf-8 -*-
"""
Created on Wed Jan 1 02:20:17 2020

@author : Paul DHALLUIN
"""

import sys
from ruler import Ruler

nom_fichier = sys.argv[1]  # pour sélectionner le fichier d'après l'entrée dans le terminal
fichier = open(nom_fichier, "r")
liste_fichier = []
for line in fichier:
    if line != "\n":        # on ne considère pas les lignes vides
        if line[-1:] == "\n":
            liste_fichier.append(line[:-1])
        else:
            liste_fichier.append(line)
if len(liste_fichier)%2 == 1:
    liste_fichier.pop(-1)        # on élimine la dernière ligne orpheline

nombre = int(len(liste_fichier)/2)
for i in range(nombre):
    ruler = Ruler(liste_fichier[2*i], liste_fichier[2*i + 1])   # on utilise la classe Ruler
    ruler.compute()
    top, bottom = ruler.report()
    print(f"====== example # {i + 1} - distance = {ruler.distance}")
    print(top)
    print(bottom)