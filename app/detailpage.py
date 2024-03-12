from kivy.uix.screenmanager import Screen
from utils import NavigationTabs
import sqlite3
from kivy.lang import Builder

Builder.load_file("detailpage.kv")
class DetailPage(Screen):
    def on_pre_enter(self, *args):
        self.display_details()

    def display_details(self):
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        pk = self.manager.current_pk
        c.execute("SELECT * FROM passwords WHERE id=?", (pk,))
        entry = c.fetchone()
        conn.close()

        if entry:
            self.ids.detail_title.text = f"{entry[1]}"
            self.ids.detail_username.text = f"{entry[2]}"
            self.ids.detail_password.text = f"{entry[3]}"
            self.ids.detail_pk.text = f"{entry[0]}"

    def edit_entry(self):
        # Set the current_pk to edit
        self.manager.current = 'create_edit'

    def delete_entry(self):
        self.manager.current = 'delete'
        # conn = sqlite3.connect('passwords.db')
        # c = conn.cursor()
        # c.execute("DELETE FROM passwords WHERE id=?", (self.manager.current_pk,))
        # conn.commit()
        # conn.close()
        #
        # # After deletion, go back to the list page
        # self.manager.current = 'list'
