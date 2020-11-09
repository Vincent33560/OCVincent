from interfaces import config_interface

question = input("Voulez vous lancer le truc ?")

if question == 0:
    lancement = config_interface()
else:
    print("ok")