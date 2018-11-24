

import os
import pickle

from Tracker_code import game_analyse

path_files = '/home/paul/Documents/projet_tracker_winamax/history_hand/'


lst_treated_file = pickle.load(open("treated_file_b", 'rb'))



for element in os.listdir(path_files):
    if element not in lst_treated_file:
        game_analyse(os.path.abspath(element))
        break
       



pickle.dump(lst_treated_file, open("treated_file_b","wb"))
