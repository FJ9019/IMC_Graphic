from kivy.uix.screenmanager import ScreenManager
from package.Data import Data

class MyScreenManager(ScreenManager):
    def check_credentials(self, pseudo:str, password:str):
        print(f"{pseudo} : {password}")
        get_user = Data.get_user(pseudo, password)
        print(get_user)
        if get_user['status']:
            self.current = "index"
    pass