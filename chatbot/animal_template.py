import json, re



class Animal:
    def __init__(self, step: float=0.0):
        self.step = "start"
        self.dialogo = self.dialog()
        self.msg = None
        self.options = None

    def anwser(self, text:str) -> str:
        print(f"person said: {text}")
        selected_option = text.lower()
        if selected_option in self.dialogo.keys():
            self.step = selected_option
        else:
            self.msg = "Opção invalida!"
            return self.msg
        
        self.msg = self.dialogo[text]["msg"]
        self.options = self.dialogo[text]["options"]

        return f"{self.msg}\n{self.options}"
    
    def iter_options(self, options):
        for option in options:
            yield option
    
    @staticmethod
    def _valid_anwser(text: str):
        if text == "":
            return True
        return False
    
    def dialog(self):
        with open("dialogo.json") as f:
            dialog_dict = json.load(f)
        return dialog_dict