
from classe_jeu import *

class Player():

    def __init__(self, name):
        self.name = name    
        self.stack = []
        self.nb_played_hand = 0
        self.nb_faced_hand = 0
        self.jeu_pf = Jeu_pf()
        self.jeu_f = Jeu_f()
        self.jeu_t = Jeu_t()
        self.jeu_r = Jeu_r()
        
        self.hand_played = False
        self.nb_talk = 0
        self.previous_action = ""
        

#-----------------actions--------------------------------

    def fold(self, tour):
        if tour == 2:
            self.jeu_pf.nb_fold +=1 
        elif tour == 3:
            self.jeu_f.nb_fold +=1 
        elif tour == 4:
            self.jeu_t.nb_fold +=1 
        elif tour == 5:
            self.jeu_r.nb_fold +=1 

    def check(self, tour):
        if tour == 2:
            self.jeu_pf.nb_check +=1 
            self.hand_played = True
        elif tour == 3:
            self.jeu_f.nb_check  +=1 
        elif tour == 4:
            self.jeu_t.nb_check  +=1 
        elif tour == 5:
            self.jeu_r.nb_check  +=1 

    def call(self, tour):
        if tour == 2:
            self.jeu_pf.nb_call +=1 
            self.hand_played = True
        elif tour == 3:
            self.jeu_f.nb_call +=1 
        elif tour == 4:
            self.jeu_t.nb_call +=1 
        elif tour == 5:
            self.jeu_r.nb_call +=1 
            
    def bet(self, tour):
        if tour == 3:
            self.jeu_f.nb_bet  +=1 
        elif tour == 4:
            self.jeu_t.nb_bet  +=1 
        elif tour == 5:
            self.jeu_r.nb_bet  +=1 
    
    def raize(self, tour):
        if tour == 2:
            self.jeu_pf.nb_raise +=1 
            self.hand_played = True
        elif tour == 3:
            self.jeu_f.nb_raise +=1 
        elif tour == 4:
            self.jeu_t.nb_raise +=1 
        elif tour == 5:
            self.jeu_r.nb_raise +=1 

#-----------------actions--------------------------------

    def check_raise(self, tour):
        if tour == 3:
            self.jeu_f.nb_check_raise +=1
        elif tour == 4:
            self.jeu_t.nb_check_raise +=1
        elif tour == 5:
            self.jeu_r.nb_check_raise +=1

    def check_call(self, tour):
        if tour == 3:
            self.jeu_f.nb_check_call +=1
        elif tour == 4:
            self.jeu_t.nb_check_call +=1
        elif tour == 5:
            self.jeu_r.nb_check_call +=1
            
    def check_fold(self, tour):
        if tour == 3:
            self.jeu_f.nb_check_fold +=1
        elif tour == 4:
            self.jeu_t.nb_check_fold +=1
        elif tour == 5:
            self.jeu_r.nb_check_fold +=1
            













