from kivy.uix.screenmanager import Screen
from utils import NavigationTabs
from kivy.app import App
import sqlite3
from kivy.lang import Builder

Builder.load_file("listpage.kv")
class ListPage(Screen):
    all_entries = []
    def on_enter(self):
        self.all_entries = self.get_list_data()
        self.filter_list('')  # Display all entries initially

    def get_list_data(self):
        # Your method to fetch data, returning a list of dicts or objects representing entries
        self.ids.list_view.data = []  # Clear existing data
        user_id = App.get_running_app().current_user['id']
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute("SELECT id, title FROM passwords WHERE user_id=?", (user_id,))
        entries = c.fetchall()
        conn.close()
        return entries

    def populate_list(self, entries):
        self.ids.list_view.data = []
        for entry in entries:
            self.ids.list_view.data.append({
                'text': entry[1],  # Assuming you want to display the title
                'on_press': lambda x=entry[0]: self.select_entry(x),
            })

    def filter_list(self, query):
        filtered_data = []
        query = query.lower()
        for entry in self.all_entries:
            if query.lower() in entry[1].lower():
                filtered_data.append(entry)
        self.populate_list(filtered_data)
        # self.ids.list_view.data = filtered_data  # Update your RecycleView data here



    def select_entry(self, pk):
        self.manager.current_pk = pk
        self.manager.current = 'detail'
