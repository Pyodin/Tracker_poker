# Tracker_poker

Ok les gars, voici le projet du tracker sur lequel j'ai bossé. C'est un peu le bordel dans le projet, mais je pense que l'algorithmie est bonne. 
A ce point, le code que j'ai écrit permet d'analiser UN fichier .txt fourni par les site de poker en ligne (c'est les même pour winamax et Pokerstar). J'ai commencer à écrire les fichier qui lancerons l'analyse sur tout un dossier contenant plein de hystory_hand.
Pour le moment, on est loin du tracker utilisable, mais on s'en rapproche.. Je pense que le gros du code est fait, il va juste falloir coder les fonctions qui traite les données que nous voulons récupérer.  

---------------------------------------------------------------------------------------------
Comment ça marche ? 

Dans le dossier py_files, il y a tout les fichiers python, chacun à son utilité.

1) Les fichier commençant par classe_* sont des descriptifs de classe. 

2) Le fichier Tracker_code.py est le fichier qui analyse un fichier .txt, et enregistre en mémoire plusieurs donnés qui servirons aux analyses statistiques. (J'utilise pickle pour la sauvegarde en mémoire).

3) Le fichier fonctions.py regroupe toutes les fonctions necessaires au fichier Tracker_code.py. (c'est le .h de ce fichier)

4) Le fichier init initialise les données du joueurs qui utilisera le tracker. 

5) Le fichier main.py (inutile pour l'instant car le projet n'est pas complet) est le fichier qui va aller chercher dans les repertoires du pc les fichiers "hystory_hand.txt", les analyser en utilisant le code de trcker_code, et pareil, enregistrer les données. (package os pour aller fouiller dans les répertoires) 

---------------------------------------------------------------------------------------------
Chose à faire pour continuer le projet:

1) Chaque fichier est une ébauche, ils peuvent tous être perfectionnés
2) Le fichier tracker sait maintenant analyser une partie, il faut maintenant qu'il calculs les statistiques importantes (taux 
de realnce au flop, etc...)
Cette partie va être compliqué puisqu'il va falloir différencier plusieurs cas, d'ou l'utilité des classes. En effet Il faut prendre en compte, qu'un joueur possède dans ses statistiques générales un jeu préflop, flop etc... puis un jeu bouton, SB, BB, etc... Mais ces info ne sont pas disjointes. (exemple: je veux savoir combien de fois un joueur à relancer préflop son bouton).
Bon courage pour cette partie.
3) Quand on sera à la partie interface graphique, ça serait cool de créer une option pour revoir les coup joués... La aussi ya bcp de boulot mais on en est pas encore la.
4) Il sera necessaire plus tard de differencier un hystory_hand.txt de wina ou de pokerstar. mais on en est pas encore la. 









