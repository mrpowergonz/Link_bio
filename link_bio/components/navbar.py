import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as color
import link_bio.styles.styles as styles
from link_bio.styles.fonts import font

def navbar()-> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("Adam", color=color.PRIMARY.value),
            rx.span("dev", color= color.SECONDARY.value),
            style= styles.navbar_title_style
        ),
        rx.text(
            "Mr.Power",
            font_family= font.DEFAULT.value,
            
        ),
        position ="sticky",#posicion que queda fija
        bg=color.CONTENT.value,    
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",#tiene prioridad y se quedaria fijado arriba
        top="0" #Para que la navbar se quede fijada cuando hagas scroll
    )