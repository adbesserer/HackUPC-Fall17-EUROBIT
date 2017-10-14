########################## I M P O R T S ##############################################

import argparse
from random import shuffle
from random import choice
from string import digits
import json

#######################################################################################
#                           T R A T A R   A R G U M E N T O S                         #
#######################################################################################

parser = argparse.ArgumentParser( prog= 'Role Assigner',usage= 'The script must be run with the following format: \n\n\tassig_roles.py --np NP \n\nwhere NP is the number of players that will be in the game\nThe minimum number of players is 10')

parser.add_argument('--np', type = int, help = 'The number of players', nargs = 1)
arg = parser.parse_args()
if arg.np == None :
	parser.print_help()
	exit()

n_players = arg.np[0]
if n_players < 10:
	parser.print_help()
	exit()

#assig = {} 	# key = MAC, value = [ID, ROLE]

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

def gen_IDs ():
	IDs = []
	for i in range(0,n_players):
		IDs.append('Player_'+str(i+1))
	return IDs	

#######################################################################################
#                                  I N   &   O U T                                #
#######################################################################################

##### R E A D   M A C S #####
#file = open('lista_macs.txt','r')
#macs = file.readlines()
#file.close()

roles 	= assign()
IDs 	= gen_IDs()
##### G E N E R A T E   R O L E S #####

#if len(macs)!=len(roles) :		#check errors
#	print('THE NUMBER OF ROLES IS UNEQUAL TO THE NUMBER OF MACS')
#	print('Roles: '+ len(roles))
#	print('MAC Addresses: '+ len(macs))
#	exit()

idrole = {}
for i in range (0,len(roles)):
	idrole[IDs[i]] = roles[i]

with open('id_role.txt','w') as outfile:
	json.dump(idrole,outfile)
	
#file = open('id_role.txt', 'w+')		#output a file with IDs and their roles
#for i in range(0,len(roles)):
#	file.write(IDs[i] + ' ' + roles[i]+'\n')
#file.close()

#file = open('id_MAC.txt', 'w+')		#output a file with IDs and their MAC Addresses
#for i in range(0,len(macs)):
#	file.write(IDs[i] + ' ' + macs[i])
#file.close()

