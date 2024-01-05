import reflex as rx
from link_bio.styles.styles import Size as Size

def navbar()-> rx.Component:
    return rx.hstack(
        rx.text(
            "Mr.Power",
            
        ),
        position ="sticky",#posicion que queda fija
        bg="lightgray",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",#tiene prioridad y se quedaria fijado arriba
        top="0" #Para que la navbar se quede fijada cuando hagas scroll
    )