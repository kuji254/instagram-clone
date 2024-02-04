import os

from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from home_page import HomePage

Window.size = (300, 600)
Builder.load_file("home_page.kv")
Builder.load_file("appbar.kv")
Builder.load_file("story_creator.kv")
Builder.load_file("bottom_nav.kv")
Builder.load_file("CircularAvatarImage.kv")
Builder.load_file("postcard.kv")
class InstagramApp(MDApp):
    def build(self):
        return HomePage()

    def on_start(self):
        self.root.dispatch("on_enter")

if __name__ == '__main__':
    InstagramApp().run()