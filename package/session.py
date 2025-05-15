import json

class Session():
    def make_session(self, data):
        with open('.Data/session.json') as file:
            json.dump(data, file)
        pass

    def get_session(self):
        with open('.Data/session.json') as file:
            data = json.load(file)
            return data
        pass

    def clear_session(self):
        data = {"status": False, "data": {"mot_de_passe": "", "pseudo": "", "nom_prenom": "", "age": None, "sex": None, "taille": None, "poids": None, "travail": ""}}
        with open('.Data/session.json') as file:
            json.dump(data, file)
        pass