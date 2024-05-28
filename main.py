class Enseignat():
#Premier class enseignat et le constructeur par defaut
        def __int__(self, nom=None, prenom=None, nbre_heur_annee=None):
            self.nom = nom
            self.prenom = prenom
            self.nbre_heur_annee = nbre_heur_annee

        def decrire(self, nom=None, prenom=None, nbre_heur_annee=None):
            print(nom,prenom,nbre_heur_annee)