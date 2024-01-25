import reflex as rx
from link_bio.styles.colors import Color as color
from link_bio.styles.styles import Size as Size
import link_bio.styles.styles as styles
import link_bio.constants as const
from link_bio.styles.colors import text_color as Textcolor
from link_bio.styles.fonts import font



#Investigar rx.link para enlace y rx.box para componente entero
def link_cards() -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.aspect_ratio(
                rx.image(
                    src="github_white.png",
                    border_radius="none",
                    padding_top=Size.ZERO.value,
                    padding_bottom=Size.ZERO.value,
                    
                ),
                loading="lazy",
                ratio=10 / 8,
                width="6em",
                height="6em",
                margin=Size.ZERO.value,
                
                
            ),
            header=rx.heading("Sloth machine", font_size=Size.DEFAULT.value, font_weight="900", color=Textcolor.BODY.value,margin_top=Size.SMALL.value,),
            footer="Sloth machine created with Python",font_size= Size.DEFAULT.value, color=Textcolor.FOOTER.value,font_family= font.DEFAULT.value,padding_top=Size.ZERO.value,padding_bottom=Size.SMALL.value,
            style=styles.style_card,
            
            
        ),
        is_external=True,
        display="flex",
        justify_content="center",
        width="100%",
        href="https://mrpower.portfoliobox.net/",


        
        
    )


