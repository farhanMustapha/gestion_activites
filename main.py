from flet import *


def main(page:Page):
    page.window.width=450
    page.title="gestion des activites"

#============ services ==================================
    
    def make_container_to_add_fournisseur_visible(e):
        page.clean()
        container_to_add_fournisseur.visible=True
        page.add(container_to_add_fournisseur)

    def make_container_to_add_Responsable_visible(e):
        page.clean()
        container_to_add_Responsable.visible=True
        page.add(container_to_add_Responsable)

    def make_container_to_add_tache_visible(e):
        page.clean()
        container_to_add_taches.visible=True
        page.add(container_to_add_taches)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#================ Views =================================================
    #on peut controler la visibiliter des containner pour organiser la page 
    container_to_add_activite=Container(
        content=Column([
                Text("ajouter activite"),
                TextField(label="le titre de l'activite"),
                Row(
                    [
                        TextField(label="date de debut",width=200),
                        TextField(label="date de fin",width=200),
                    ]
                ),
                Row(
                    [
                        ElevatedButton("ajouter",on_click=...),
                        ElevatedButton("Etape suivante",on_click=make_container_to_add_fournisseur_visible)
                    ]
                )
                
                
            ]
        ) 
    )

        
    container_to_add_fournisseur=Container(
        #cette interface permet de ajouter un fournisseur 
        #un fournisseur ou prestataire peux nous fournir plusieur document 
        content=Column([
                Text("ajouter fournisseur ou plus "),
                TextField(hint_text="raison social"),
                TextField(hint_text="le type de prestation",multiline=True),
                Dropdown(
                        width=250,
                        hint_text="affecter une activiter",
                        options=[
                            dropdown.Option("activite 1"),
                            dropdown.Option("activite 2"),
                            dropdown.Option("activite 3"),
                            dropdown.Option("activite 4")
                        ],
                ),
                Row(
                    [
                        TextField(label="doc a demander"),
                        #cette button doit ajouter une autre input pour saisr le nom de doc a demander s'il y a plusieur doc a demander pour chaque fournisseur 
                        TextButton("add",icon="add")
                    ]
                ),
                Dropdown(
                        width=250,
                        hint_text="paiement",
                        options=[
                            dropdown.Option("Oui"),
                            dropdown.Option("Non")
                        ],
                ),
                Row(
                    [
                        ElevatedButton("Etape precedente",on_click=...),
                        ElevatedButton("ajouter",on_click=...),
                        ElevatedButton("Etape suivante",on_click=make_container_to_add_Responsable_visible)
                    ]
                )
            
            ]
        ),
        visible=False   
    )

    container_to_add_Responsable=Container(
        #cette interface permet d'ajouter un responsable 
        content=Column([
                Text("ajouter un responsable ou plus"),
                TextField(hint_text="le nom responsable ou les responsable"),
                Dropdown(
                        width=250,
                        hint_text="fonction",
                        options=[
                            dropdown.Option("admin"),
                            dropdown.Option("charger de projet"),
                            dropdown.Option("coordinateur"),
                            dropdown.Option("animateur"),
                            dropdown.Option("autre")
                        ],
                ),
                Row(
                    [
                        ElevatedButton("Etape precedente",on_click=...),
                        ElevatedButton("ajouter",on_click=...),
                        ElevatedButton("Etape suivante",on_click=make_container_to_add_tache_visible)
                    ]
                )
                
            ]
        ),
        
        visible=False   
    )

    container_to_add_taches=Container(
        #cette interface permet de creer des taches et les affecter a un responsable 
        #un seul responsable peux etre charger par plusieur taches 
        content=Column(
            [
                Text("gerer les taches"),
                Row(
                    [
                        TextField(label="creer une tache"),
                        #ajouter input pour les taches de plus 
                        TextButton(icon="add")
                    ]
                ),
                Dropdown(
                        width=250,
                        hint_text="responsable de la tache",
                        options=[
                            dropdown.Option("admin"),
                            dropdown.Option("charger de projet"),
                            dropdown.Option("coordinateur"),
                            dropdown.Option("animateur"),
                            dropdown.Option("autre")
                        ],
                ),
                Row(
                    [
                        ElevatedButton("Etape precedente",on_click=...),
                        ElevatedButton("ajouter",on_click=...),
                        ElevatedButton("Dashbord",on_click=...)
                    ]
                )
            ]
        ),
        visible=False
    ) 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ===========home =====================================================   
    page.add(
        container_to_add_activite
    )
    page.update()

app(target=main)