cat = object
cachorro = object
def generate_anwser(animal: str, step: int):
    interactor = None
    if animal == "cat":
        interactor = cat
    elif animal == "cachorro":
        interactor = cachorro
