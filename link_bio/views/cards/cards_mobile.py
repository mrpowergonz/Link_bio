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


def cards_mobile() -> rx.Component:
    
    def create_card(title: str, footer: str, image: str, imagez: str, url: str) -> rx.Component:
        return alternative(title, footer, image, imagez, url)


    mobile_cards = [
            rx.mobile_and_tablet( 
                rx.vstack(
                    rx.heading(("Proyectos"),
                            color=Textcolor.HEADER.value,
                            text_align='center',
                            margin_bottom="0.5em",
                            margin_left="-1.5em",
                            padding_top="2em",
                            font_family=font.DEFAULT.value,
                            style=styles.title_style),
                    rx.hstack(
                        rx.box(
                            create_card(
                                "Cryptoverse", "Web page for ranking cryptocurrencies", "github_white.png", "react.png",
                                const.GITHUB4_URL),
                            width="75%",
                            justify='center',
                            align='center',
                            margin_bottom="1em",
                            style=styles.style_card_mobile
                        ),
                        rx.box(
                            create_card(
                                "Sloth machine", "Sloth machine built in Python", "github_white.png", "python.png",
                                const.GITHUB1_URL),
                            width="75%",
                            justify='center',
                            align='center',
                            margin_bottom="1em",
                            style=styles.style_card_mobile
                        ),
                    ),
                    rx.hstack(
                        rx.box(
                            create_card(
                                "To do app", "Take notes, App built in Django", "github_white.png", "django.png",
                                const.GITHUB2_URL),
                            width="75%",
                            justify='center',
                            align='center',
                            margin_bottom="1em"
                            
                        ),
                        rx.box(
                            create_card(
                                "Password generator", "App built in Javascript, create your own password", "github_white.png",
                                "javascript.png",
                                const.GITHUB3_URL),
                            width="75%",
                            justify='center',
                            align='start',
                            style=styles.style_card_mobile,
                            margin_bottom="1em"
                        ),
                        
                    ),
                    rx.hstack(
                        rx.box(
                            create_card(
                                "Portfolio", "Personal webpage", "github_white.png", "reflex.png",
                                const.GITHUB6_URL),
                            width="75%",
                            justify='center',
                            align='center',
                        ),
                        rx.box(
                            create_card(
                                "Booking", "CSS styles for a booking web page", "github_white.png", "css.png",
                                const.GITHUB5_URL),
                            width="75%",
                            justify='center',
                            align='center',
                            margin_left="-4em",
                            margin_bottom="-5em",
                            
                        ),
                    ),
                    justify='center',
                    
                
                    align='center', 
                    margin_top="2em",
                    margin_bottom="2em",
                    margin_left="0.5em",
                    style=styles.style_card_mobile
                ),
                width="100%",
                margin_left="1em",
                margin_bottom="1em",
            ),
        ]
    return rx.hstack(*(mobile_cards))