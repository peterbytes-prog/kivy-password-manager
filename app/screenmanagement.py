from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from listpage import ListPage
from deletepage import DeletePage
from createeditpage import CreateEditPage
from detailpage import DetailPage
from homepage import HomePage
from utils import NavigationTabs
from kivy.lang import Builder

Builder.load_file("screenmanagement.kv")


class ScreenManagement(ScreenManager):
    def update_nav(self, navigator):
        for i in navigator.children:
            if self.current == i.key:
                i.state = 'down'
                i.disabled = True
    def reset_nav_buttons(self, navigator):
        for i in navigator.children:
            if self.current != i.key:
                i.state = 'normal'
                i.disabled = False

    pass
