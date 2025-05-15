from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from package.session import Session

from kivy.properties import StringProperty, NumericProperty, ObjectProperty

Builder.load_file("update_page.kv")


class UpdatePage(BoxLayout):
    pseudo = StringProperty()
    nom_prenom = StringProperty()
    age = NumericProperty()
    sex = StringProperty()
    travail = StringProperty()
    taille = StringProperty()
    poids = StringProperty()

    password = StringProperty()

    def preload_data(self):
        session = Session.get_session()
        if session['status']:
            data = session['data']
            self.pseudo = data['pseudo']
            self.nom_prenom = data['nom_prenom']
            self.age = str(data['age'])
            self.taille = str(data['taille'])
            self.poids = str(data['poids'])
            self.travail = data['travail']
            self.sex = "Hommes" if data['sex'] ==0 else "Femmes"
            
            print(session)
        pass
    pass
