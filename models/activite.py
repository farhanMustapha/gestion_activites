from flet import *

class Activite(Column):
    def __init__(self,titre,date_d,date_f):
        self.titre=titre
        self.dateDebut=date_d
        self.dateFin=date_f



    def shaow_detail(self):
        return f"titre : {self.titre} ,Date de debut : {self.dateDebut} , Date de fin {self.dateFin}"
        
        