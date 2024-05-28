class Enseignat():
#Premier class enseignat et le constructeur par defaut
    def __int__(self, nom=None, prenom=None, nbre_heur_annee=None):
        self.nom = nom
        self.prenom = prenom
        self.nbre_heur_annee = nbre_heur_annee
        self.salaire=100
    def decrire(self):
        print(f"Cet enseignant est {self.nom}, {self.prenom},{self.nbre_heur_annee}")
    def payer(self,montant):
        print(f"On vient de payer l'enseignant {montant}")
    """POLYMORPHISME"""
class Assistant(Enseignat):
    """POLYMORPHISME"""
    def decrire(self, nom=None, prenom=None, nbre_heur_annee=None):
        print(f"Celui ci est un assistant {nom}, {prenom},{nbre_heur_annee}" )
        """SURCHAGE"""
    def payer(self):
        super().payer(montant=100)
