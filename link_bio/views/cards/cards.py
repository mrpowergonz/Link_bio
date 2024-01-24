import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_cards import link_cards

def cards() -> rx.Component:
    return link_cards()