class Fournisseur:
    def __init__(self,name,description):
        self.name=name
        self.description=description
        self.activites=[]
        self.docs=[]
        self.paiment=False