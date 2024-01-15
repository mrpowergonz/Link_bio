import reflex as rx

from link_bio.styles.styles import Size as size

def link_tech(imagen: str, url: str)-> rx.Component:
    return rx.link(
        rx.image(
            heigh=size.VERY_BIG.value,
            src=imagen
        ),
        href=url,
        is_external=True
    )