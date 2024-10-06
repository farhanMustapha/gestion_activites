from flet import *

class Activite(Column):
    def __init__(self):
        super().__init__()
        self.new_activite=TextField(label="nouveau activite"),
            
        self.div_show_activite=Column()

        self.controls=[
            Column(
                [
                    self.new_activite,
                    ElevatedButton("+",on_click=...)
                ]
            )
        ]