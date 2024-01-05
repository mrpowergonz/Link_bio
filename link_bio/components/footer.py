import reflex as rx
import datetime #para pasar el año en el que estamos al footer
from link_bio.styles.styles import Size as Size

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"2020-{datetime.date.today().year} Mr. Power by Adam Power",
                href="https://mrpower.portfoliobox.net/",
                is_external=True,  #para que se abra en una nueva pagina
                font_size= Size.MEDIUM.value
        ),
        rx.text(
            " building web pages from Burgos to the world",
            margin_top="0px  !important",
            font_size= Size.MEDIUM.value
            ),
        margin_bottom=Size.BIG.value
    )