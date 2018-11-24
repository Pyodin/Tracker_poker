# -*- coding: utf-8 -*-

from classe_coup import *
from classe_joueur import *



#-----------------fonctions --------------------------------

def test_line(line):
        if len(line) > 1:
                if line[1] == "Poker" : return 0
                elif line[1] == "ANTE/BLINDS": return 1
                elif line[1] == "PRE-FLOP": return 2
                elif line[1] == "FLOP": return 3
                elif line[1] == "TURN": return 4
                elif line[1] == "RIVER" : return 5
                elif line[1] == "SHOW" : return 6
                elif line[1] == "SUMMARY": return 7
                else: return -1
        else: return -1

#--------------------init-----------------------------------

def init_table(line, coup, partie):
        if line[0] == "Table:": 
                coup.position_bouton = get_position_b(line) 
            
        elif line[0] == "Seat":
                coup.nb_player += 1
                name = get_name(line)
                stack = get_stack(line)

                if get_name(line) not in partie.name_player_met:
                        new_player = create_player(name, partie)
                        new_player.stack.append( get_stack(line) )
                        coup.players.append( new_player )
                else:
                        index = get_index( get_name(line), partie )
                        old_player = partie.player_met[index]
                        old_player.stack.append(stack)
                        old_player.nb_talk = 0

                        coup.players.append( old_player )

                

def get_position_b(line):
        position = int( line[-4][1] )
        return position

def get_stack(line):
        stack = int( line[-1][1:-1] )
        return stack

def get_index(name, partie):
        seat = 0
        for i in partie.player_met:
                if i.name == name: return seat
                else: seat += 1
        return seat

def get_name(line):
        temp = line[2:-1]
        name = ""
        for i in temp: name += i + " "
        return name[:-1]

def create_player(name, partie):
        new_player = Player(name)

        partie.player_met.append( new_player )
        partie.name_player_met.append(name)
        return new_player

#-----------------------------------------------------------

def get_player(line, coup):
        player = 0
        for i in coup.players:
                if i.name in lst_to_str(line):
                        player = i
                        return player
                        break


def get_action(line, player, tour):
        if "folds" in line:
                action = "fold"
        elif "checks" in line:
                action = "check"
        elif "calls" in line:
                action = "call"
        elif "raises" in line:
                action = "raise"
        elif "bets" in line:
                action = "bet"
        else: action = "error"
        return action


def lst_to_str(line):
        lst = ""
        for i in line:
                lst += i + " "
        return lst[:-1]


#-----------------------------------------------------------

def do_action(action, player, tour):
        if action == "fold":
                player.fold(tour)
        elif action == "check":
                player.check(tour)
        elif action == "bet":
                player.bet(tour)
        elif action == "call":
                player.call(tour)
        elif action == "raise":
                player.raize(tour)
        player.nb_talk +=1
        player.previous_action = action


def do_action2(action, player, tour):
        pervious_action = player.previous_action

        if pervious_action == "check":
                if action == "fold":
                        player.check_fold(tour)
                elif action == "call":
                        player.check_call(tour)
                elif action == "raise":
                        player.check_raise(tour)

        player.nb_talk +=1
        player.previous_action = action

#-----------------preflop-----------------------------------

def analyse_pf(line, coup, tour):
        if line[0] == "***": 
                init_tour_players(coup)
        else:
                player = get_player(line, coup)
                action = get_action(line, player, tour)
                if player.nb_talk == 0:
                        player.jeu_pf.nb_jeu_pf +=1
                        do_action(action, player, tour)

                elif player.nb_talk == 1:
                        do_action2(action, player, tour)


#-----------------flop--------------------------------------

def analyse_f(line, coup, tour):
        if line[0] == "***": 
                init_tour_players(coup)
        else:
                player = get_player(line, coup)
                action = get_action(line, player, tour)

                if player.nb_talk == 0:
                        player.jeu_f.nb_jeu_f +=1
                        do_action(action, player, tour)

                elif player.nb_talk == 1:
                        do_action2(action, player, tour)
         

#-----------------turn--------------------------------------

def analyse_t(line, coup, tour):
        if line[0] == "***": 
                init_tour_players(coup)
        else:
                player = get_player(line, coup)
                action = get_action(line, player, tour)

                if player.nb_talk == 0:
                        player.jeu_t.nb_jeu_t +=1
                        do_action(action, player, tour)

                elif player.nb_talk == 1:
                        do_action2(action, player, tour)
         

#-----------------river-------------------------------------

def analyse_r(line, coup, tour):
        if line[0] == "***": 
                init_tour_players(coup)
        else:
                player = get_player(line, coup)
                action = get_action(line, player, tour)

                if player.nb_talk == 0:
                        player.jeu_r.nb_jeu_r +=1
                        do_action(action, player, tour)

                elif player.nb_talk == 1:
                        do_action2(action, player, tour)

                        
#-----------------------------------------------------------
#-----------------------------------------------------------


def get_hand_faced(coup, me):
        for i in coup.players:
                if i.hand_played == True and me.hand_played == True:
                        i.nb_faced_hand +=1
                        
        for i in coup.players:
                i.hand_played = False
                i.previous_action = ""

def init_tour_players(coup):
        for i in coup.players:
                i.nb_talk = 0

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------
