from asyncio import selector_events
from base64 import encode
import json
from typing import List


class Animal:
    def __init__(self, step: float=0.0):
        self.step = "start"
        self.dialogo = self.dialog()
        self.msg = None
        self.options = ["gato", "cachorro"]
        self.order: List = []

    def anwser(self, text:str) -> str:
        print(f"options are: {self.options}")
        selected_option = text.lower()
        if selected_option == "reiniciar":
            self.order = []
        elif selected_option == "continuar":
            self.step = self.order[-1]
            selected_option = self.step
        elif selected_option in self.options and not selected_option in self.dialogo.keys():
            self.step = "fim"
            self.order.append(selected_option)
            selected_option = "fim"
            self.options = self.order
        elif selected_option in self.options and selected_option in self.dialogo.keys():
            self.step = selected_option
            self.order.append(selected_option)
        else:
            self.step = "invalido"
            selected_option = "invalido"
        
        self.msg = self.dialogo[selected_option]["msg"]
        if selected_option != "fim":
            self.options = self.dialogo[selected_option]["options"] #if 
            self.step = "reiniciar"
        else:
            self.options = self.order
        options = "<br>-" + "<br>-".join(self.options)

        print(f"person said: {text}")
        print(self.order)

        return f"{self.msg}\n{options}"
    
    def dialog(self):
        with open("dialogo.json", encoding="utf-8") as f:
            dialog_dict = json.load(f)
        return dialog_dict