########################## I M P O R T S ##############################################

import argparse
from random import shuffle

#######################################################################################
#                           T R A T A R   A R G U M E N T O S                         #
#######################################################################################

parser = argparse.ArgumentParser( prog= 'Role Assigner',usage= 'The script must be run with the following format: \n\n\tassig_roles.py --np NP \n\nwhere NP is the number of players that will be in the game\nThe minimum number of players is 10')

parser.add_argument('--np', type = int, help = 'The number of players', nargs = 1)
n_players = parser.parse_args().np[0]
if n_players == None or n_players < 10:
	parser.print_help()
	exit()

#######################################################################################
#                                D E F F U N C S                                      #
#######################################################################################

def assign ():
	nurses    = ['Nurse']    * int(0.1*n_players)
	guards    = ['Guard']    * int(0.1*n_players)
	wolves    = ['Wolf']     * int(0.2*n_players)
	villagers = ['Villager'] * (n_players - len(nurses) - len(guards) - len(wolves))
	roles = nurses+guards+wolves+villagers
	shuffle(roles)
	return roles


#######################################################################################
#                                       M A I N                                       #
#######################################################################################

file = open('Roles_List.txt', 'w+')
roles = assign()
for r in roles:
	file.write(r+'\n')
file.write('-')	
file.close()

