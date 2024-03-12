from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.app import App
import sqlite3
import bcrypt

from kivy.uix.boxlayout import BoxLayout
from utils import NavigationTabs
from kivy.lang import Builder

Builder.load_file("Homepage.kv")

class HomePage(Screen):
    def show_login_popup(self):
        login_popup = LoginPopup()
        login_popup.open()

    def show_signup_popup(self):
        signup_popup = SignupPopup()
        signup_popup.open()


class LoginPopup(Popup):
    def login(self, *args, **kwargs):
        self.process_login(self.ids.login_username.text, self.ids.login_password.text)
    def process_login(self, username, password):
        if not username or not password:
            self.ids.login_status.text = 'Username and password required.'
            return
        # Assuming you have a method to check credentials:
        if self.check_credentials(username, password):
            self.dismiss()  # Close the popup on successful login
            App.get_running_app().root.current = 'list'  # Navigate to the main screen
        else:
            self.ids.login_status.text = 'Invalid username or password.'

    def check_credentials(self, username, password):
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        stored_password = cursor.fetchone()
        conn.close()

        if stored_password and bcrypt.checkpw(password.encode('utf-8'), stored_password[0]):
            return True
        return False

class SignupPopup(Popup):
    def signup(self, *args, **kwargs):
        self.process_signup( self.ids.signup_username.text, self.ids.signup_password.text, self.ids.signup_password_confirm.text)
    def process_signup(self, username, password, confirm_password):
        # print(username, password, confirm_password)
        if not username or not password or not confirm_password:
            self.ids.signup_status.text = 'All fields are required.'
            return
        if password != confirm_password:
            self.ids.signup_status.text = 'Passwords do not match.'
            return
        # Add more validations as needed

        # Assuming you have a method to add a new user:
        if self.add_user(username, password):
            self.ids.signup_status.text = 'Account Created'
            self.dismiss()  # Close the popup on successful signup
            App.get_running_app().SCRMGMT.current = 'list'

            # Possibly show a success message or directly log in the user
        else:
            self.ids.signup_status.text = 'Username already taken.'

    def add_user(self, username, password):
        # Check if the username is taken
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE username=?", (username,))
        if cursor.fetchone():
            conn.close()
            return False

        # Hash the password before storing
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert the new user
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return True
