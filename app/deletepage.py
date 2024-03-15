from kivy.uix.screenmanager import Screen
from kivy.app import App
# from utils import NavigationTabs
from kivy.lang import Builder
import sqlite3

Builder.load_file("deletepage.kv")
class DeletePage(Screen):
    def delete_entry(self):
        user_id = App.get_running_app().current_user['id']
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute("DELETE FROM passwords WHERE id=? AND user_id=?", (self.manager.current_pk, user_id,))
        conn.commit()
        conn.close()

        self.manager.current_pk = 0  # Reset current_pk after deletion
        self.manager.current = 'list'
