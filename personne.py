import datetime
from time import strftime


class Enfant:
    @classmethod
    def newObj(cls):
        self = cls.__new__(cls)
        return self

    # Initialiser les attributs d'un objet Enfant
    def __init__(self, id, nom, prenom, sexe, dateNaiss):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.dateNaiss = dateNaiss

class Personne:
    #Une liste des Personnes qui va contenir des objet Personne
    listDesPersonnes = []

    @classmethod
    def makeit(cls):
        self = cls.__new__(cls)
        return self

    #Initialiser les attributs d'un objet Personne
    def __init__(self,id, nom, prenom, sexe,year,month,day, pere, mere):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.year = year
        self.month = month
        self.day = day
        self.dateNaiss = datetime.date(self.year,self.month,self.day).strftime("%A, %B %d, %Y")
        self.pere = pere
        self.mere = mere
        self.listDesEnfants = []

    # Methode Ajouter qui ajoute un objet dans la liste des personnes
    @classmethod
    def AjouterPersonne(cls):
        id = int(input("Entrer l'id: "))
        nom = input("Entrer le nom: ")
        prenom = input("Entrer le prenomnom: ")
        sexe = input("Entrer le sexe: ")
        year = int(input("Entrer l'anne' de naissance: "))
        month = int(input("Entrer le mois de naissance: "))
        day = int(input("Entrer le jour de naissance: "))
        pere = input("Entrer le nom de pere: ")
        mere = input("Entrer le nom de mere: ")
        per = Personne(id,nom,prenom,sexe,year,month,day,pere,mere)
        Personne.listDesPersonnes.append(per)

    # Methode Supprimer qui supprime un objet dans la liste des personnes
    @staticmethod
    def SupprimerPersonne():
        id = int(input("Entrez l'id pour Supprimer: "))
        for obj in Personne.listDesPersonnes:
            if obj.id == id:
                Personne.listDesPersonnes.remove(obj)
                break

    # Methode Modifier qui modifie tous les attributs d'un objet
    @staticmethod
    def ModifierPersonne():
        id = int(input("Entrez l'id pour Modifier: "))
        for obj in Personne.listDesPersonnes:
            if obj.id == id:
                obj.id = int(input("Entrer le nouveau id: "))
                obj.nom = input("Entrer le nouveau nom: ")
                obj.prenom = input("Entrer le nouveau prenom: ")
                obj.sexe = input("Entrer le nouveau sexe: ")
                obj.year = int(input("Entrer le nouveau annee de naissance: "))
                obj.month = int(input("Entrer le nouveau mois de naissance: "))
                obj.day = int(input("Entrer le nouveau jour de naissance: "))
                obj.dateNaiss = datetime.date(obj.year, obj.month, obj.day).strftime("%A, %B %d, %Y")
                obj.pere = input("Entrer le nouveau nom de pere: ")
                obj.mere = input("Entrer le nouveau nom de mere: ")

    ## Methode NbrEnf qui retourne le nombre des enfants d'un personne
    def NbrEnf(self): return len(self.listDesEnfants)

    # Methode RetourneInfos qui retourn tous les attributs
    def RetourneInfos(self):
        return f"Id: {self.id}\nNom: {self.nom}\nPrenom: {self.prenom}\nSexe: {self.sexe}\n" \
               f"Date de naisance : {self.dateNaiss}\nNombre D'enfants : {Personne.NbrEnf(self)}\n"

    # Methode Afiiche qui affiche tous les attributs
    def Affich(self): print(self.RetourneInfos())

    # Methode Rechercher qui recherche un personne dans la liste des personnes
    @staticmethod
    def Rechercher():
        choice = input("Si vous voulez Rechercher par id Tappez (i)\n"
                       +"Si vous voulez Rechercher par nom Tappez (n)\n"
                       +"Si vous voulez Rechercher par prenom Tappez (p)")
        if choice.lower() == 'i':
            id = int(input("Entrer le id de personne: "))
            for obj in Personne.listDesPersonnes:
                if obj.id == id: Personne.Affich(obj)
        elif choice.lower() == 'n':
            nom = input("Entrer le nom de personne: ")
            for obj in Personne.listDesPersonnes:
                if obj.nom == nom: Personne.Affich(obj)
        elif choice.lower() == 'p':
            prenom = input("Entrer le prenom de personne: ")
            for obj in Personne.listDesPersonnes:
                if obj.prenom == prenom: Personne.Affich(obj)
        else: print("Erreur d'entree!")

    # Methode qui affiche tous les Personnes de la liste des personnes
    @staticmethod
    def AfficherTsPers():
        cpt = 0
        for obj in Personne.listDesPersonnes:
            Personne.Affich(obj)
            cpt += 1
            print(cpt)

    # Methode qui affiche le pere et la mere d'un personne
    @staticmethod
    def RetournerPereMere():
        id = int(input("Entrez l'id du personne que vous voulez connaisser leur nom pere et mere: "))
        for obj in Personne.listDesPersonnes:
            if obj.id == id:
                print(f"Le Pere de {obj.nom} est {obj.pere}")
                print(f"La Mere de {obj.nom} est {obj.mere}")

    # Methode qui affiche l'age d'un personne
    @staticmethod
    def RetournerAge():
        id = int(input("Entrez l'id du personne que vous voulez connaisser leur age "))
        for obj in Personne.listDesPersonnes:
            if obj.id == id:
                today = datetime.date.today()
                age = today.year - obj.year
                print(f"L'age de {obj.nom} est {age} ans")

    # Methode qui permet d'ajouter un enfant dans la liste des enfants
    @staticmethod
    def AjouterEnfant():
        nb = 'o'
        id = int(input("Entrer l'id de personne"))
        while (nb != 'n'):
            for obj in Personne.listDesPersonnes:
                if obj.id == id:
                    ide = int(input("Entrer l'id de l'enfant: "))
                    nom = input("Entrer le nom de l'enfant: ")
                    prenom = input("Entrer le prenom de l'enfant: ")
                    sexe = input("Entrer le sexe de l'enfant: ")
                    dateNaiss = input("Entrer la date de naissance de l'enfant: ")
                    enfa = Enfant(ide, nom, prenom, sexe, dateNaiss)
                    obj.listDesEnfants.append(enfa)
            nb = input("Voulez vous ajouter un nouveau enfant? o/n")

    # Methode qui permet d'afficher les enfants dans la liste des enfants
    @staticmethod
    def AfficherEnfs():
        id = int(input("Entrer l'id de personne"))
        for obj in Personne.listDesPersonnes:
            if obj.id == id:
                print(f"Les enfants de {obj.nom} sont:")
                for enf in obj.listDesEnfants:
                    print("Id :" + str(enf.id))
                    print("Nom: " + enf.nom)
                    print("Prenom: " + enf.prenom)
                    print("Sexe: " + enf.sexe)
                    print("Date de naissance: " + enf.dateNaiss)
                    print("")

    # Methode qui permet d'enregistrer les infos d'un personne dans un fichier .txt
    @staticmethod
    def Sauvegarder():
        id = int(input("Entrer l'id de personne"))
        path = input("Entrer le nom de fichier")
        for obj in Personne.listDesPersonnes:
            if obj.id == id:
                with open(path+".txt", "w+") as file:
                    file.write(Personne.RetourneInfos(obj))
                    file.close()

    # Methode TrierPrs qui permet de Trier la liste des personnes par nom (ou par id en cas d'egalite)
    @staticmethod
    def TrierPrs(): Personne.listDesPersonnes.sort(key=lambda x: (x.nom, x.id))

#Menu pour choisir
def Menu():
    choice = None
    while choice != -1:
        print("**************************Gestion des Personnes************************")
        print("***          Entrez 1 pour Ajouter un Personne                      ***")
        print("***          Entrez 2 pour Supprimer un Personne                    ***")
        print("***          Entrez 3 pour Modifier un Personne                     ***")
        print("***          Entrez 4 pour Consulter la liste des Personnes         ***")
        print("***          Entrez 5 pour Chercher un Personne                     ***")
        print("***          Entrez 6 pour Retourner le Pere et Mere d'un Personne  ***")
        print("***          Entrez 7 pour Retourner l'Age d'un Personne            ***")
        print("***          Entrez 8 pour Trier la liste des Personnes             ***")
        print("***          Entrez 9 pour Sauvegarder les donnes                   ***")
        print("***********************************************************************")

        print("**************************Gestion des Enfants**************************")
        print("***          Entrez 10 pour Ajouter un Enfant                       ***")
        print("***          Entrez 11 pour Afficher les enfants d'un personne      ***")
        print("***          Entrez 12 pour Imprimer l'acte                         ***")
        print("***********************************************************************")
        print("***          Entrez -1 pour Quitter le programme                    ***")
        print("***********************************************************************")
        choice = int(input("Votre choix?: "))

        Personne.AjouterPersonne() if choice == 1 else \
            Personne.SupprimerPersonne() if choice == 2 else \
                Personne.ModifierPersonne() if choice == 3 else \
                    Personne.AfficherTsPers() if choice == 4 else \
                        Personne.Rechercher() if choice == 5 else \
                            Personne.RetournerPereMere() if choice == 6 else \
                                Personne.RetournerAge() if choice == 7 else \
                                    Personne.TrierPrs() if choice == 8 else \
                                        Personne.Sauvegarder() if choice == 9 else \
                                            Personne.AjouterEnfant() if choice == 10 else \
                                                Personne.AfficherEnfs() if choice == 11 else \
                                                    Personne.RetournerPereMere() if choice == 12 else \
                                                        print("Au revoir")  if choice == -1 else \
                                                            print("Nombre invalide! veuillez ressayer")


def Start():
    mdp = "m"
    cpt = 3
    cpt2 = cpt - 1
    print("**************************Gestion des actes d'état civil numérisés************************")
    userMdp = input("Veuillez entre le mot de passe pour acceder au systeme: ")
    for i in range(cpt - 1):
        if userMdp != mdp:
            userMdp = input(f"Mot de passe invalide! veuillez ressayer a nouveau! (il vous reste {cpt2} chances) ")
            cpt2 -= 1
        elif userMdp == mdp:
            Menu()
            break







