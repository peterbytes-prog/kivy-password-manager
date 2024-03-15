from kivy.uix.screenmanager import Screen
from utils import NavigationTabs
from kivy.app import App
import sqlite3
from kivy.lang import Builder

Builder.load_file("listpage.kv")
class ListPage(Screen):
    def on_enter(self):
        self.populate_list()

    def populate_list(self):
        self.ids.list_view.data = []  # Clear existing data
        user_id = App.get_running_app().current_user['id']
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute("SELECT id, title FROM passwords WHERE user_id=?", (user_id,))
        entries = c.fetchall()
        for entry in entries:
            self.ids.list_view.data.append({
                'text': entry[1],  # Assuming you want to display the title
                'on_press': lambda x=entry[0]: self.select_entry(x),
            })
        conn.close()

    def select_entry(self, pk):
        self.manager.current_pk = pk
        self.manager.current = 'detail'
