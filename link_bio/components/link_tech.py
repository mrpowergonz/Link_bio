import reflex as rx
from link_bio.styles.colors import Color as color
from link_bio.styles.styles import Size as size

def link_tech(imagen: str, url: str ,alt: str)-> rx.Component:
    return rx.link(
        rx.image(
            heigh=size.BIG.value,
            src=imagen,
            width="150px",
            margin_bottom="10px",
           
             _hover={
            "cursor": "pointer",
            "transform": "scale(1.15)",
            
            },
            transition= "0.5s",
        ),
        
      
        href=url,
        is_external=True
    )