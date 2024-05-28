"""ABSTRACTION"""
from abc import ABC
class Personnel(ABC):
    def conges(self):
        print("est en conges")
class Enseignat(Personnel):
#Premier class enseignat et le constructeur par defaut
        def __int__(self, nom=None, prenom=None, nbre_heur_annee=None):
            self.nom = nom
            self.prenom = prenom
            self.nbre_heur_annee = nbre_heur_annee

        def decrire(self, nom=None, prenom=None, nbre_heur_annee=None):
            print(nom,prenom,nbre_heur_annee)
    """HERITAGE"""
#Deuxième class enseignat chercheur qui herite la class Enseingant

class Enseignat_chercheur(Enseignat):
        def __init__(self,heur_complem_cherch):
            self.heur_complem_cherch=heur_complem_cherch
#Fonction qui calcule le salaire de chercheur
        def calculer_salire_cherch(self,heur_complem_cherch):
            if heur_complem_cherch>192:
                resultat=(2000*12)+heur_complem_cherch*40
            elif heur_complem_cherch<=192:
                resultat=(2000*12)
            return resultat

#Troisième class enseignant vacateur qui herite  de la class  Enseignat
class Enseignant_vacataire(Enseignat):
        def __init__(self,heure_vacataire):
            self.heure_vacataire=heure_vacataire
#Fonction qui calcule le salaire de vacateur
        def calculer_salaire_vacataire(self,heure_vacataire):
            resultat=heure_vacataire*40
            return resultat
#Quatrième class de doctorant qui herite de la class Enseingant
class Enseignant_doctorat(Enseignat):
        def __init__(self,heure_doctorat):
            self.heure_doctorat=heure_doctorat
#Fonction qui calcule  le salaire de docteur
        def calculer_salaire_doctorat(self,heure_doctorat):
            if heure_doctorat<=96:
                resultat =heure_doctorat * 30
            elif heure_doctorat>96:
                resultat = 96 * 30
            return resultat
