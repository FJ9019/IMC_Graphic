from kivy.uix.screenmanager import ScreenManager
from package.Data import Data
from package.User import User
from package.session import Session


class MyScreenManager(ScreenManager):
    def get_gender(self, sex):
        if sex == "Homme":
            return 0
        elif sex == "Femme":
            return 1
        
    def check_credentials(self, pseudo:str, password:str):
        print(f"{pseudo} : {password}")
        get_user = Data.get_user(pseudo, password)
        print(get_user)
        if get_user['status']:
            self.current = "index"
            Session.make_session(get_user)

    def check_signup(self, pseudo, password:str, password_repeat, nom_prenom, age, sex, taille, poids, travail):

        if password != "" and password == password_repeat:
            user = User(pseudo, password, nom_prenom, int(age), self.get_gender(sex), int(taille)/100, int(poids), travail)
            data = Data(user)
            data.update()
            print("Inscription réussie")
            self.current = "index"
            get_user = Data.get_user(pseudo, password)
            Session.make_session(get_user)
        pass

    def update_data(self):
        self.current = "update"
        pass
    pass