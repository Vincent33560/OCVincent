from interfaces import Interfaces

question = input("Voulez vous lancer le truc ?")

if question == 0:
    lancement = Interfaces()
else:
    print("ok")