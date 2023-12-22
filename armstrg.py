
#fonction d'armstrong modif test zahra
def armstrg(ch):
    try:
        if verif(ch)== False:
            print("Le nombre est  invalide")
        else:
            b=0
            for i in range(len(ch)):
                b = b + int(ch[i])**3
#                print(b)
            if b == int(ch):
                return 1   
            else:
                 return 0
    except ValueError: 
        return -1
 #       print("Un erreur se produit.") 

#fonction verification
def verif(arg1):
    try:
        if arg1.isnumeric() == False :
            return False
        else:
            if int(arg1) > 0 :
                return True
            else:
                return False
    except ValueError: 
#        print("Un erreur se produit.") 
        return False
