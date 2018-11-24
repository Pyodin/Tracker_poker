

class Partie():
    nb_partie = -1

    def __init__(self, name_player_met, player_met):
        Partie.nb_partie += 1
        self.name_player_met = name_player_met
        self.player_met = player_met




class Coup():
        nb_coup = 0
              
        def __init__(self):
                Coup.nb_coup += 1
                self.players = []
                self.nb_player = 0
                self.position_bouton = 0

        def affiche(self):
            print "nombre de coup:", self.nb_coup
            print "nombre de joueur dans le coup:", self.nb_player
            print "position du bouton:", self.position_bouton
        



