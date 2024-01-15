import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import text_color as Textcolor
from link_bio.styles.fonts import font
from link_bio.styles.colors import Color as Color

def header()-> rx.Component:
        return rx.vstack(
                #Para que se quede alado del icono
            rx.hstack(
                rx.avatar(
                        name="Adam Power",
                        size="xl",
                        src="logo.png",
                        color=Textcolor.BODY.value,
                        bg=Color.BACKGROUND2.value,
                        padding="2px",
                        border="4px",
                        border_color=Color.PRIMARY.value, #color del borde del avatar
                        
                ),
                rx.vstack(
                        rx.heading(
                                "Adam Power", 
                                size="lg",
                                color=Textcolor.HEADER.value,
                                font_family= font.TITLE.value,
                        ),
                        rx.text(
                                "@mr___power",
                                margin_top=Size.ZERO.value,
                                color=Textcolor.BODY.value,
                                font_family= font.DEFAULT.value,
                                
                        ),
                        rx.hstack(
                        link_icon("https://github.com/mrpowergonz"),
                        link_icon("https://github.com/mrpowergonz"),
                        ),
                        align_items="start" ,
                        
                      
                ),
                spacing=Size.DEFAULT.value,
        ),


        rx.flex(
                    info_text("+2 " , "años de experiencia"),
                    rx.spacer(),
                    info_text("+2 " , "años de experiencia"),
                    rx.spacer(),
                    info_text("+2 " , "años de experiencia"),
                    width="100%",
                    font_family= font.DEFAULT.value,
        ),
               
        rx.text(
            "Soy un programador autodidacta que esta intentando aprender todas las ultimas tecnologias. Aqui os dejo todos mis enlaces de interés. Bienvenid@! ",
            color=Textcolor.BODY.value,
            font_family= font.DEFAULT.value,
            font_size = Size.MEDIUM1.value,

        ),
            spacing=Size.BIG.value, #Spacing para darle espacio a todos los componentes
            align_items="start"
               
        )
