"""
Un script python de verification d'un nombre est armstrong ou non
NB : un nombre positif est appelé un nombre d’Armstrong s’il est égal à la somme des cubes de ses chiffres, par exemple 0, 1, 153, 370, 371, 407, etc.
"""

import armstrg
import sys

print("Bienvenue dans notre programme.\n")

def run_armstrg():
    term = input("Entrer un entier \n")
    res = armstrg.armstrg(term)
    if res != None:
        print(res)
        if res == 1:
            print(term + " est un nombre d'Armstrong")
        else:
            if res == 0 :
                print("{} n'est pas un nombre d'Armstrong".format(term))
            else :
                print("Un erreur se produit.") 
        
        #print( term + " n'est pas un nombre d'Armstrong")
        keep_going = input(
            "Voulez-vous stopper le programme ? Écrivez Oui, dans ce cas\n"
        )
        if keep_going == "Oui":
            sys.exit(0)
    print("Nous allons recommencer le programme\n")
    run_armstrg()


run_armstrg()
