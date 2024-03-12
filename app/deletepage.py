from kivy.uix.screenmanager import Screen
from utils import NavigationTabs
from kivy.lang import Builder
import sqlite3

Builder.load_file("deletepage.kv")
class DeletePage(Screen):
    def delete_entry(self):
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute("DELETE FROM passwords WHERE id=?", (self.manager.current_pk,))
        conn.commit()
        conn.close()

        self.manager.current_pk = 0  # Reset current_pk after deletion
        self.manager.current = 'list'
