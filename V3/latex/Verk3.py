# -*- coding: cp1252 -*-
from priority_dict import priority_dict
from bisect import bisect_left
import time
import sys

class verk3:

    """
    FG:
    notSpan er listi sem inniheldur þá leggi sem eru ekki í minnsta spantrénu
    Span er listi inniheldur þá leggi sem eru í minnsta span trénu
    wholeNet er listi sem inniheldur alla leggi í netinu
    tree er listi sem inniheldur alla hnúta sem eru í minnsta span trénu
    """


    def __init__(self):
        self.notSpan = []
        self.Span = []
        self.wholeNet = []
        self.tree = []

    """
    Fyrir:  Ekkert
    Eftir:  Búið er að prenta út vigtina á minnsta spantrénu og næstminnsta
            spantré fyrir hvern legg
    """
    def inputToDict(self):
        ...
    

    """
    Fyrir: G er net hnúta og r er upphafshnútur í netinu
    Eftir: Búið er að finna minnsta spantré fyrir G og vigt þess
    """
    def MSTPRIM(self,G,r):
        ...


    """
    Fyrir: G er net hnúta og w er vigt minnsta spantrés
    Eftir: Búið er að finna og prenta út N-1 minnstu spantrén.
    """
    def NotMinPRIM(self,G,w):

        ...

"""
Fyrir: G er net hnúta, u er hnútur og v er foreldi hnútsins í minnsta spantrénu
Eftir: Búið er að skipta minnsta  spantrénu upp í tvo samhengisþætti og finna minni samhengisþáttinn
"""

def doubleBFS(G,u,v):
    ...    


def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end    
    

if __name__ == '__main__':
    V3 = verk3()
    V3.inputToDict()

