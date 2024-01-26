import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_cards import link_cards
from link_bio.components.link_cards import alternative,alternative_card
from link_bio.styles.styles import Size as Size
import link_bio.constants as const

def create_card(title:str,footer:str,image: str,imagez, url: str) -> rx.Component:
   # return link_cards( ),
    return alternative(title,footer,image,imagez,url)

def cards() -> rx.Component:
    all_cards = [
        create_card("Sloth machine","Sloth machine built in Python","github_white.png","python.png",const.GITHUB_URL),
        create_card("To do app","App built in Django","github_black.png","django.png",const.GITHUB_URL),
        create_card("Password generator","App built in Javascript","github_black.png","javascript.png",const.GITHUB_URL),
        
]
    return rx.hstack(*all_cards)