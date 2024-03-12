from kivy.app import App
from kivy.properties import ObjectProperty
from utils import NavigationTabs
from model import init_db
from screenmanagement import ScreenManagement

# Main App class
class PasswordManagerApp(App):
    SCRMGMT = ObjectProperty()

    def change_screen(self, screen_name):
        print(self.SCRMGMT.current, screen_name)
        # Check if the root widget is available
        if self.SCRMGMT:
            if (self.SCRMGMT.current != screen_name):
                 self.SCRMGMT.current = screen_name
            else:
                print('already', screen_name)

        else:
            print("ScreenManager is not yet initialized.")
        return self.SCRMGMT.current

    def build(self):
        self.SCRMGMT = ScreenManagement()

        return self.SCRMGMT

# Run the app
if __name__ == '__main__':
    init_db()
    PasswordManagerApp().run()
