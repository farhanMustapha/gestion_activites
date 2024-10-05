from flet import *
#from activites.models.activite import *


def main(page:Page):
    page.window.width=450
    page.title="creer une activite"
    page.window.left=740

    titre_of_activite=TextField(hint_text="le titre de l'activite")
    btn_to_add_activite=ElevatedButton("ajouter",on_click=...)
    page.add(
        titre_of_activite,
        btn_to_add_activite
    )
    page.update()

app(target=main)