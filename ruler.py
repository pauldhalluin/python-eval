# -*- coding: utf-8 -*-
"""
Created on Wed Jan 1 00:00:36 2020

@author : Paul DHALLUIN
"""

import numpy as np
from colorama import Fore, Style

def red_text(text: str) -> str:
    """
        Permet d'écrire en rouge pour mettre en valeur les différences
    """
    return f"{Fore.RED}{text}{Style.RESET_ALL}"

class Ruler:
    
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
    
    def compute(self):
        """
            Crée la matrice de similarité
            Calcule également la distance pour l'alignement optimal
        """
        l1 = len(self.str1)
        l2 = len(self.str2)
        d = 1
        F = np.zeros((l1 + 1, l2 + 1))
        for i in range(l1 + 1):
            F[i][0] = d*i
        for j in range(l2 + 1):
            F[0][j] = d*j
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if self.str1[i - 1] == self.str2[j - 1]:
                    Choice1 = F[i-1][j-1]
                else:
                    Choice1 = F[i-1][j-1] + 1
                Choice2 = F[i-1][j] + d
                Choice3 = F[i][j-1] + d
                F[i][j] = min(Choice1, Choice2, Choice3)
        self.F = F
        self.distance = F[-1][-1]   # on la retrouve dans le coin de la matrice

    def report(self):
        """
            Détermine le meilleur alignement des chaines de caractères
            Retourne les deux chaines de caractères en question
        """
        d = 1
        STR1 = ""
        STR2 = ""
        l1 = len(self.str1)
        l2 = len(self.str2)        
        M = self.F
        i = l1
        j = l2
        while i > 0 and j > 0:
            score = M[i][j]
            score_diagonal = M[i-1][j-1]
            score_up = M[i][j-1]
            score_left = M[i-1][j]
            if self.str1[i-1] == self.str2[j-1]:
                ajout = 0
            else:
                ajout = 1
            if score == score_diagonal + ajout:
                STR1 = self.str1[i-1] + STR1
                STR2 = self.str2[j-1] + STR2
                i -= 1
                j -= 1
            elif score == score_left + d:
                STR1 = self.str1[i-1] + STR1
                STR2 = '=' + STR2
                i -= 1
            elif score == score_up + d:
                STR1 = '=' + STR1
                STR2 = self.str2[j-1] + STR2
                j -= 1   
        while i > 0:
                STR1 = self.str1[i-1] + STR1
                STR2 = '=' + STR2
                i -= 1
        while j > 0:
                STR2 = self.str2[j-1] + STR2
                STR1 = '=' + STR1
                j -= 1
        Mot1 = ""
        Mot2 = ""
        for lettre1, lettre2 in zip(STR1, STR2):
            if lettre1 == lettre2:
                Mot1 += lettre1
                Mot2 += lettre2
            else:
                Mot1 += red_text(lettre1)    # la disctinction permet de mettre 
                Mot2 += red_text(lettre2)    # les différences en rouge
        return Mot1, Mot2