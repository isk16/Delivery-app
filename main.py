from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen, SwapTransition
import random
import qrcode
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
import matplotlib.pyplot as plt
import mysql.connector
from datetime import datetime
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDListBottomSheet
import json
import requests



# print(datetime.now().strftime('%d_%B_%Y_%I_%M_%S '))

class gener_code(Screen):
    def genQR(self):
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )  # créer le code QR vide
        rand_key =10000000000 * random.random()
        # print(int(rand_key ))
        # print(type(rand_key ))
        img = qrcode.make(str(rand_key ))
        qr.add_data(rand_key)  # on peut inserer le code unique pour chaque commande directement ici

        # self.ids["qr_data"].text = ''
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        plt.imshow(img)
        time=datetime.now().strftime('%d_%B_%Y_%I_%M_%S ')
        plt.imsave(time+'image_new.png',img,cmap=plt.cm.gray )



class COMMANDE(Screen):
    pass


class CODEQR(Screen):
    def __init__(self, **kwargs):
        super(CODEQR, self).__init__(**kwargs)

    def CHANG(self, text):
        print(self.ids.code_liv.text)

    def check_code(self,text):
        pass
#    verification le code lu avec celui de la base de donnée
class SettingsScreen(Screen):
    pass


class Historique(Screen):
    def callback_for_menu_items(self, *args):
        toast(args[0])

    def show_example_list_bottom_sheet(self):
        bottom_sheet_menu = MDListBottomSheet()
        for i in range(1, 11):
            bottom_sheet_menu.add_item(
                f"Standart Item {i}",
                lambda x, y=i: self.callback_for_menu_items(
                    f"Standart Item {y}"
                ),
            )
        bottom_sheet_menu.open()


# historique des commandes depuis la base des données

class MenuScreen(Screen):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class main(MDApp):
    # url de notre base de donnée fire base
    url='https://i-sal1603-default-rtdb.firebaseio.com/.json'


    def patch(self ):
        # premet de converter vers format json
        strr={"http://example.org/about": {
                    "http://purl.org/dc/terms/title": [{
                        "type": "literal",
                        "value": "Anna's Homepage"
                    }]
                }
            }
        print(strr)
        to_database= json.loads(str(strr))
        # envoie les données json vers la base de donnée Firebase
        requests.patch(url=self.url, json=to_database)

    def on_start(self):
        pass

    def build(self):
        pass

if __name__ == "__main__":
    main().run()
