import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_tech import link_tech
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import text_color as Textcolor
from link_bio.styles.fonts import font

def tech() -> rx.Component:
    return rx.vstack(
        title("Tecnologias"),
        rx.hstack(
            rx.vstack(
                link_tech(
                    "javascript.png",
                    const.JAVASCRIPT_URL,
                ),
                rx.text(
                    "JAVASCRIPT",
                    margin_top=Size.ZERO.value,
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    align_self="flex_start",
                ),

                link_tech(
                    "python.png",
                    const.PYTON_URL,
                
                ),
            ),
            width="50%",
            align_items="start",
            border_radius="3px",
            border_color="white",
        ),
    )