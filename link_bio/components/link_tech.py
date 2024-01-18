import reflex as rx
from link_bio.styles.colors import Color as color
from link_bio.styles.styles import Size as size

def link_tech(imagen: str, url: str ,)-> rx.Component:
    return rx.link(
        rx.image(
            heigh=size.BIG.value,
            src=imagen,
            width="150px",
            margin_button="18px",
            transition="0.2s",
           
             _hover={
            "cursor": "pointer",
            "transform": "scale(1.15)",
           
            },
        ),
      
        href=url,
        is_external=True
    )