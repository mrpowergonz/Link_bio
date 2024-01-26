import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_cards import link_cards
from link_bio.components.link_cards import alternative
from link_bio.styles.styles import Size as Size
import link_bio.constants as const

def cards() -> rx.Component:
   # return link_cards( ),
    return alternative(
        "github_white.png",
        const.GITHUB_URL
    )