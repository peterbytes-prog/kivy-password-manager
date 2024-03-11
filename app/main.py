# Main App class
class PasswordManagerApp(App):
    def build(self):
        return ScreenManagement()

# Run the app
if __name__ == '__main__':
    PasswordManagerApp().run()
