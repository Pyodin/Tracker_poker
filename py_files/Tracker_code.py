

from fonctions import *
import pickle
from init import me



def game_analyse(file0):

    file0 = open(str(file0), "r")

    previous_partie = pickle.load( open("previous_partie_b","rb") )
    name_player_met = previous_partie.name_player_met
    player_met = previous_partie.player_met

    partie = Partie(name_player_met, player_met)

    buff, tour = 0,0

    for line in file0:
        line = line.split()

        buff = test_line(line)

        if buff != -1: tour = buff

            #---------------------nvx coup----------------------
        if tour == 0: 
            if buff == 0: 
                coup = Coup()
            init_table(line, coup, partie) # ok

            #---------------------preflop----------------------
        elif tour == 2 and line != []:             
            analyse_pf(line, coup, tour)

            #---------------------flop-------------------------
        elif tour == 3 and line != []: 
            analyse_f(line, coup, tour)

            #---------------------turn-------------------------
        elif tour == 4 and line != []: 
            analyse_t(line, coup, tour)

            #---------------------river------------------------
        elif tour == 5 and line != []: 
            analyse_r(line, coup, tour)

            #---------------------SUMMARY----------------------
        """
        elif tour == 7 and line != []:
            get_hand_faced(coup, me)
        """
    pickle.dump(partie, open("previous_partie_b","wb"))

    file0.close()



game_analyse("history_hand/20180923_WANTED(248506286)_real_holdem_no-limit.txt")
