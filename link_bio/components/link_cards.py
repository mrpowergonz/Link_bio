import reflex as rx
from link_bio.styles.colors import Color as color
from link_bio.styles.styles import Size as Size
import link_bio.styles.styles as styles
import link_bio.constants as const


def link_cards()-> rx.Component:
      return rx.vstack(
        rx.card(
            rx.aspect_ratio(rx.image(src="github_white.png", border_radius="none",margin_bottom="1em"),loading="lazy", ratio=10 / 8, width="160px",),
            header=rx.heading( "Sloth machine",font_size=Size.MEDIUM.value,  font_weight="900"),
            footer ="",
            style=styles.style_card,
        ),
        is_external=True,
        # centeamos la tarjeta en el espacio 
        display="flex",
        justify_content="center", 
      )