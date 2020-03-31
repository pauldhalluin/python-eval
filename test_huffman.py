# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:45:57 2020

@author: Paul DHALLUIN
"""

""" Ce code correspond au test fourni sur nbhosting"""

from codec import TreeBuilder, Codec

text = "a dead dad ceded a bad babe a beaded abaca bed"

# on analyse les fréquences d'occurrence dans le texte
# pour fabriquer un arbre binaire
builder = TreeBuilder(text)
binary_tree = builder.tree()

# on passe l'arbre binaire à un encodeur/décodeur
codec = Codec(binary_tree)

# qui permet d'encoder
encoded = codec.encode(text)

# et de décoder
decoded = codec.decode(encoded)

# si cette assertion est fausse il y a un gros problème avec le code
assert text == decoded

# on affiche le résultat
print(f"{text}\n{encoded}")
if decoded != text:
    print("OOPS")