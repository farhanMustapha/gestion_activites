from flet import *


def main(page:Page):
    page.window.width=450
    page.title="gestion des activites"

    
    def make_container_to_add_fournisseur_visible(e):
        page.clean()
        container_to_add_fournisseur.visible=True
        page.add(container_to_add_fournisseur)

    def make_container_to_add_Responsable_visible(e):
        page.clean()
        container_to_add_Responsable.visible=True
        page.add(container_to_add_Responsable)



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
        content=Column([
                Text("ajouter fournisseur ou plus "),
                TextField(hint_text="raison social"),
                TextField(hint_text="le type de prestation"),
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
                        ElevatedButton("ajouter",on_click=...),
                        ElevatedButton("Etape suivante",on_click=make_container_to_add_Responsable_visible)
                    ]
                )
            
            ]
        ),
        visible=False   
    )

    container_to_add_Responsable=Container(
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
                ElevatedButton("ajouter",on_click=...)
                
            ]
        ),
        
        visible=False   
    ) 
        
    
    

    page.add(
        container_to_add_activite,container_to_add_fournisseur,container_to_add_Responsable
    )
    page.update()

app(target=main)