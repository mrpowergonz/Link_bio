import reflex as rx
from link_bio.styles.styles import Size as Size 

def link_icon(image: str, url: str, alt: str)-> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.DEFAULT.value,
            alt=""
        ),
        href=url,
        is_external=True
    )