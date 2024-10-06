class Responsable:
    def __init__(self,name,fonction):
        self.name_resp=name
        self.fonction_resp=fonction


    def show_details(self):
        return f" le nom responsable {self.name_resp} , sa fonction {self.fonction_resp}"