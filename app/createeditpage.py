from kivy.uix.screenmanager import Screen
from utils import NavigationTabs
from kivy.lang import Builder
import sqlite3

Builder.load_file("createeditpage.kv")
class CreateEditPage(Screen):
    def on_pre_enter(self, *args):
        # Load entry details if editing
        if self.manager.current_pk > 0:  # 0 is default for new entries
            self.load_entry_details()
        else:
            self.clear_form()

    def load_entry_details(self):
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute("SELECT * FROM passwords WHERE id=?", (self.manager.current_pk,))
        entry = c.fetchone()
        conn.close()

        if entry:
            self.ids.title_input.text = entry[1]
            self.ids.username_input.text = entry[2]
            self.ids.password_input.text = entry[3]

    def clear_form(self):
        self.ids.title_input.text = ''
        self.ids.username_input.text = ''
        self.ids.password_input.text = ''

    def save_or_update_entry(self):
        title = self.ids.title_input.text
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        if self.manager.current_pk > 0:  # Update existing entry
            c.execute("UPDATE passwords SET title=?, username=?, password=? WHERE id=?",
                      (title, username, password, self.manager.current_pk))
        else:  # Insert new entry
            c.execute("INSERT INTO passwords (title, username, password) VALUES (?, ?, ?)",
                      (title, username, password))
        conn.commit()
        conn.close()
        self.clear_form()
        self.manager.current_pk = 0  # Reset current_pk
        self.manager.current = 'list'
