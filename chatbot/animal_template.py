import json


class Animal:
    def __init__(self, step: float=0.0):
        self.step = "start"
        self.dialogo = self.dialog()
        self.msg = None
        self.options = ["gato", "cachorro"]

    def anwser(self, text:str) -> str:
        print(f"options are: {self.options}")
        print(f"person said: {text}")
        selected_option = text.lower()
        #if selected_option in self.dialogo.keys():
        if selected_option in self.options:
                self.step = selected_option
        else:
            self.msg = "Opção invalida!"
            return self.msg
        
        self.msg = self.dialogo[selected_option]["msg"]
        self.options = self.dialogo[selected_option]["options"]
        options = "<br>-" + "<br>-".join(self.options)

        return f"{self.msg}\n{options}"
    
    def dialog(self):
        with open("dialogo.json") as f:
            dialog_dict = json.load(f)
        return dialog_dict