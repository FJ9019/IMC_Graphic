from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label

from package.session import Session

Builder.load_file("login_page.kv")


class LoginPage(BoxLayout):
    msg = StringProperty()
    def check_session(self, widget: Label):
        session = Session.get_session()
        status = session['status']

        if not status:
            widget.text = "Utilisateur non trouvé"
            widget.opacity = 1
        pass
    pass
