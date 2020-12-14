__authors__ = ("Vincent Da Costa")

__contact__ = ("vincent.dacosta33@outlook.fr")

__version__ = "1.0.0"

# Projet 6 OPENCLASSROOMS
## Participez à la vie de la communauté Open Source

Ce script fonctionne sur les routeurs CISCO via ios, il nécéssite la création d'un utilisateur et d'un mot de passe au préalable afin de pouvoir établir la connexion SSH.

## Installation
Exemple de création de l'accès SSH sur le routeur :
https://reussirsonccna.fr/configuration-du-ssh-sur-ios/

Préparez vous à lancer le script depuis un machine connectée au même réseau que le routeur.
Sur une machine linux vous devrez installer python avec la commande ```apt-get install python3```.
Installer le pip de python avec la commande ```apt install python-pip``` pour pouvoir installer ensuite le module paramiko 
avec la commande ```pip3 install paramiko```
 Vous pouvez maintenant lancer le script avec la commande ```python3 main.py```, suivez simplement les instructions affichées dans le prompt.


## Usage

Vous devrez aussi modifier dans le fichier utils.py à la ligne 52 le mot de passe de votre
utilisateur du router cisco.

```python
send(shell, "vdcvdc\n")
```



## License
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr)


