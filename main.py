class Enseignat():
#Premier class enseignat et le constructeur par defaut
        def __int__(self, nom=None, prenom=None, nbre_heur_annee=None):
            self.__nom = nom
            self.__prenom = prenom
            self.__nbre_heur_annee = nbre_heur_annee

        def decrire(self, nom=None, prenom=None, nbre_heur_annee=None):
            print(nom,prenom,nbre_heur_annee)