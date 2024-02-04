from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

class PostCard(MDCard):
    username = StringProperty()
    profile_pic = StringProperty()
    avatar = StringProperty()
    caption = StringProperty()
    post = StringProperty()
    likes = StringProperty()
    comments = StringProperty()
    posted_ago = StringProperty()