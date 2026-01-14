from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.add_widget(Label(text="🏢 Dadar Land Admin", font_size=22))
        self.add_widget(Label(text="Seeni", font_size=18))

        self.username = TextInput(hint_text="Username", multiline=False)
        self.password = TextInput(hint_text="Password", password=True, multiline=False)

        self.add_widget(self.username)
        self.add_widget(self.password)

        self.login_btn = Button(text="Seeni", background_color=(0, 0.5, 0, 1))
        self.login_btn.bind(on_press=self.check_login)
        self.add_widget(self.login_btn)

        self.status = Label(text="")
        self.add_widget(self.status)

    def check_login(self, instance):
        if self.username.text == "admin" and self.password.text == "123":
            self.status.text = "✅ Milkiin seente!"
            self.clear_widgets()
            self.show_dashboard()
        else:
            self.status.text = "⚠️ Username ykn Password dogoggora!"

    def show_dashboard(self):
        self.add_widget(Label(text="📊 Dashboard", font_size=22))
        self.add_widget(Label(text="💰 Galii: 0 ETB"))
        self.add_widget(Label(text="👥 Maamiltoota: 0"))
        self.add_widget(Label(text="👷 Ogeeyyii: 0"))

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    MyApp().run()
