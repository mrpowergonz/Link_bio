import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as color
from link_bio.styles.colors import text_color as Textcolor

def info_text(title: str, body: str)-> rx.Component:
    return rx.box(
        rx.span(
            title, 
            font_weigh="bold", 
            color=color.PRIMARY.value,
        ),
        f"{body}", 
        font_size= Size.MEDIUM.value,
        color=Textcolor.BODY.value,
    )