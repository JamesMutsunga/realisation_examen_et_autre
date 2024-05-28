class Enseignat():
#Premier class enseignat et le constructeur par defaut
    def __int__(self, nom=None, prenom=None, nbre_heur_annee=None):
        self.nom = nom
        self.prenom = prenom
        self.nbre_heur_annee = nbre_heur_annee
    def decrire(self):
        print(f"Cet enseignant est {self.nom}, {self.prenom},{self.nbre_heur_annee}")
    """POLYMORPHISME"""
class Assistant(Enseignat):
    def decrire(self, nom=None, prenom=None, nbre_heur_annee=None):
        print(f"Celui ci est un assistant {nom}, {prenom},{nbre_heur_annee}" )