#!/usr/bin/env python3
import random

# La idea en principio es que este script genere un fichero de texto a ser leido por PHP

#print('Welcome to the lobby')
#print('Introduce el numero de elementos a ser desplegado')
n = input()
liste = {}
n_lobo = 20
n_enfermera = n_policia = 10
n_habitante = 60

def assign_role():
    r = random.randint(0,100)
    if (r <= n_enfermera*2):
        r = random.randint(0,100)
        if (r <= 50):
            role = "Nurse"
        else:
            role = "Guard"
    elif (r <= n_lobo):
        role = "Wolf"
    elif (r <= n_habitante):
        role = "Villager"
    return role


for x in range (0, n):
    role = assign_role()
    liste[x] = role


#print "Player ID and role:"

for key, value in liste.items():
    print (key, value)
