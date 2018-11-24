
"""
from classe_jeu import * 

class Position(Jeu_pf, Jeu_f, Jeu_t, Jeu_r):
    p_fold = 0
    p_check = 0
    p_call = 0
    p_raiz = 0
    p_limp = 0

    def fold(self):
        self.p_fold +=1

    def check(self):
        self.p_check +=1

    def call(self):
        self.p_call +=1

    def raiz(self):
        self.p_raiz +=1

    def limp(self):
        self.p_limp +=1



class Position_BB(Position):
    nbr_BB = 0
    def __init__(self):
        self.position = "BB"
        self.nbr_BB +=1

"""
"""
class Position_SB(Position):
    nbr_SB = 0
    def __init__(self):
        self.position = "SB"
        self.nbr_SB +=1

class Position_BT(Position):
    nbr_BT = 0
    def __init__(self):
        self.position = "BT"
        self.nbr_BT +=1

class Position_CO(Position):
    nbr_CO = 0
    def __init__(self):
        self.position = "CO"
        self.nbr_CO +=1

class Position_UTG(Position):
    nbr_UTG = 0
    def __init__(self):
        self.position = "UTG"
        self.nbr_UTG +=1



"""
