
import pickle
from fonctions import create_player
from classe_coup import *

user_name = "paul bzh"
name_player_met = []
player_met = []



partie = Partie(name_player_met, player_met)
pickle.dump(partie, open("previous_partie_b","wb"))

lst_treated_file = []
pickle.dump(lst_treated_file, open("treated_file_b","wb"))


me = create_player(user_name, partie)














