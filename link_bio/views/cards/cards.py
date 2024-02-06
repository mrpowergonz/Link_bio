import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_cards import link_cards
from link_bio.components.link_cards import alternative,alternative_card
from link_bio.styles.styles import Size as Size
import link_bio.constants as const
from link_bio.styles.styles import Size as Size, Textcolor
from link_bio.styles.fonts import font
import link_bio.styles.styles as styles
from link_bio.styles.styles import title_card_style, style_card_mobile


def cards() -> rx.Component:
    
    def create_card(title: str, footer: str, image: str, imagez: str, url: str) -> rx.Component:
        return alternative(title, footer, image, imagez, url)

    desktop_cards = [
        rx.desktop_only(
        rx.container(
            rx.heading(("Proyectos"),
                       color=Textcolor.HEADER.value,
                       text_align='right',
                       margin_bottom="30px",
                       margin_left="-3.5em",
                       padding_top="4em",
                       font_family=font.DEFAULT.value,
                       style=styles.title_style),
            rx.hstack(
                rx.box(
                    create_card(
                        "Cryptoverse", "Web page for ranking cryptocurrencies", "github_white.png", "react.png",
                        const.GITHUB4_URL),
                    width="200%",
                    justify='center',
                    align='start'
                ),

                rx.box(
                    create_card(
                        "Sloth machine", "Sloth machine built in Python", "github_white.png", "python.png",
                        const.GITHUB1_URL),
                    width="200%",
                    margin_left="-6em",
                    style=styles.title_card_style
                ),

                rx.box(
                    create_card(
                        "To do app", "Take notes, App built in Django", "github_white.png", "django.png",
                        const.GITHUB2_URL),
                    width="200%",
                    margin_left="-2em"
                ),
                width="300%",
                margin_left="15em",
                margin_bottom="3em",
            ),

            rx.hstack(
                rx.box(
                    create_card(
                        "Password generator", "App built in Javascript, create your own password", "github_white.png",
                        "javascript.png",
                        const.GITHUB3_URL),
                    width="100%",
                    justify='center',
                    align='start'
                ),

                rx.box(
                    create_card(
                        "Portfolio", "Personal webpage", "github_white.png", "reflex.png",
                        const.GITHUB6_URL),
                    width="100%"
                ),

                rx.box(
                    create_card(
                        "Booking", "CSS styles for a booking web page", "github_white.png", "css.png",
                        const.GITHUB5_URL),
                    width="100%",
                    margin_left="-4em"
                ),
                width="300%",
                margin_left="15em",
                margin_bottom="7em",
            ),

            justify='center',
            align='start',
            center_content=True,
            margin_top="1em",
            margin_bottom="-6em",
            width="100%",
            align_items="center",
            margin_left="-5em",
            ),
        ),
    ]

   

    return rx.hstack(*(desktop_cards))
