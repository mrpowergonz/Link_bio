import reflex as rx
import datetime #para pasar el año en el que estamos al footer
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import text_color as Textcolor
from link_bio.styles.colors import Color as Color
from link_bio.styles.fonts import font

def footer()-> rx.Component:
    return rx.vstack(
        
        rx.avatar(
                name="Adam Power",
                size="2xl",
                src="logo.png",
                color=Textcolor.BODY.value,
                bg=Color.BACKGROUND2.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value,
            alt="Logotipo MR.Power. Mi silueta en un diafragma de fotografia"
            ),
        rx.link(f"2020-{datetime.date.today().year} Mr. Power by Adam Power",
                href="https://mrpower.portfoliobox.net/",
                is_external=True,  #para que se abra en una nueva pagina
                font_size= Size.MEDIUM.value,
                font_family= font.DEFAULT.value,
                
        ),
        rx.text(
            " building web pages from Burgos to the world",
            font_family= font.DEFAULT.value,
            margin_top=Size.ZERO.value,
            font_size= Size.MEDIUM.value,
            ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        color=Textcolor.FOOTER.value,
        padding_left="2em",
        )
    


def footer_mobile()-> rx.Component:
    return rx.vstack(
           rx.mobile_only(
                rx.avatar(
                        name="Adam Power",
                        size="2xl",
                        src="logo.png",
                        color=Textcolor.BODY.value,
                        bg=Color.BACKGROUND2.value,
                        padding="2px",
                        border="4px",
                        border_color=Color.PRIMARY.value,
                    alt="Logotipo MR.Power. Mi silueta en un diafragma de fotografia"
                    ),
               rx.box (
                    rx.text(
                        " building web pages",
                        font_family= font.DEFAULT.value,
                        margin_top=Size.SMALL.value,
                        font_size= Size.MEDIUM.value,
                        ),
                        width="100%"
                ),
                rx.box(
                    rx.text(
                        "from Burgos to",
                        font_family= font.DEFAULT.value,
                        margin_top=Size.SMALL.value,
                        font_size= Size.MEDIUM.value,
                        
                        ),
                    margin_left="1em"
                ),
                rx.box(
                    rx.text(
                        "the world",
                        font_family= font.DEFAULT.value,
                        margin_top=Size.SMALL.value,
                        font_size= Size.MEDIUM.value,
                        
                        ),
                    margin_left="2em"
                ),
                rx.link(f"2020-{datetime.date.today().year} Mr. Power",
                    href="https://mrpower.portfoliobox.net/",
                    is_external=True,  #para que se abra en una nueva pagina
                    font_size= Size.MEDIUM.value,
                    font_family= font.DEFAULT.value,
                        
                ),
                
            ),
                margin_bottom=Size.SMALL.value,
                padding_x=Size.SMALL.value,
                color=Textcolor.FOOTER.value,
                margin_left="13em"
        )