# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 15:52:43 2020

@author: Paul DHALLUIN
"""

def poids_caracteres(chaine: str) -> list:
    """
        Prend en argument un texte et renvoie une liste contenant
        les lettres présentes et leurs nombres d'apparition organisés
        dans un format adapté pour la suite du code
    """
    dictio = {}
    for caractere in chaine:
        if caractere not in dictio.keys(): 
            dictio[caractere] = 1
        else: 
            dictio[caractere] += 1
    liste = []
    for lettre in dictio.keys():       # pour chaque lettre on donne comme infos son 
        liste.append([dictio[lettre], [[lettre, ""]]])  # poids et le début du code binaire
        liste.sort()    # on place les lettres les moins récurrentes en premier
    return(liste)

class TreeBuilder:
    
    def __init__(self, texte): 
        self.texte = texte
        self.caracteres = poids_caracteres(texte)
    
    def tree(self) -> dict:
        """
            Construit l'arbre binaire
        """
        liste_noeuds = self.caracteres          # le format des noeuds et des
        while len(liste_noeuds) > 1:            # feuilles est semblable afin
            n1 = liste_noeuds.pop(0)            # de faciliter leur manipulation
            n2 = liste_noeuds.pop(0)
            for lettre in n1[1]:
                lettre[1] = "0" + lettre[1]     # le chemin d'accès binaire est
            for lettre in n2[1]:                # construit progressivement
                lettre[1] = "1" + lettre[1]
            n = [n1[0] + n2[0], n1[1] + n2[1]]  # les noeuds possèdent les infos
            liste_noeuds.append(n)              # de toutes les feuilles au-dessous
            liste_noeuds.sort()
        dictio = {}
        for lettre in liste_noeuds[0][1]:
            dictio[lettre[0]] = lettre[1]
        return dictio

class Codec:
    
    def __init__(self, arbre_binaire):
        self.arbre = arbre_binaire
        
    def encode(self, texte: str) -> str:
        """
            Encode le texte
        """
        code = ""
        for lettre in texte:
            code += self.arbre[lettre]
        return code
    
    def decode(self, code: str) -> str:
        """
            Décode le code binaire
        """
        dictio = self.arbre
        inv_arbre = {v: k for k, v in dictio.items()}   # on inverse le dictionnaire
        texte = ""
        while len(code) > 0:
            existence_lettre = False
            longueur = 1
            while existence_lettre == False:
                if code[:longueur] in inv_arbre.keys(): # on détecte où se termine le
                    existence_lettre = True             # code de la lettre
                else:
                    longueur += 1
            key = code[:longueur]
            code = code[longueur:]                      # on réduit le code à décoder
            texte += inv_arbre[key]
        return texte